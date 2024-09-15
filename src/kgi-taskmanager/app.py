import streamlit as st
import pandas as pd
import json
from datetime import datetime, timedelta
from recurring_tasks import handle_recurring_tasks
from notifications import send_notification
import os

# Path to the tasks data
TASK_DATA_PATH = "src/kgi-taskmanager/data/tasks.json"

# CSS for styling
def add_custom_css():
    st.markdown("""
        <style>
        .high-priority {color: red;}
        .medium-priority {color: orange;}
        .low-priority {color: green;}
        </style>
    """, unsafe_allow_html=True)

# Load tasks from JSON file
def load_tasks():
    if os.path.exists(TASK_DATA_PATH):
        with open(TASK_DATA_PATH, 'r') as file:
            return json.load(file)
    return []

# Save tasks to JSON file
def save_tasks(tasks):
    with open(TASK_DATA_PATH, 'w') as file:
        json.dump(tasks, file, indent=4)

# Display tasks with color-coded priority
def display_tasks(tasks):
    st.subheader("Task List")
    for task in tasks:
        priority_class = ""
        if task['priority'] == "High":
            priority_class = "high-priority"
        elif task['priority'] == "Medium":
            priority_class = "medium-priority"
        else:
            priority_class = "low-priority"

        st.markdown(f"<p class='{priority_class}'>{task['name']} - Due: {task['due_date']}</p>", unsafe_allow_html=True)
        st.write(f"Priority: {task['priority']} | Recurring: {task['recurring']}")

# Add a new task
def add_task(tasks):
    st.sidebar.subheader("Add New Task")
    task_name = st.sidebar.text_input("Task Name")
    priority = st.sidebar.selectbox("Priority", ["High", "Medium", "Low"])
    due_date = st.sidebar.date_input("Due Date", datetime.now())
    recurring = st.sidebar.selectbox("Recurring", ["None", "Daily", "Weekly", "Monthly"])

    if st.sidebar.button("Add Task"):
        new_task = {
            'name': task_name,
            'priority': priority,
            'due_date': due_date.strftime('%Y-%m-%d'),
            'recurring': recurring,
            'completed': False
        }
        tasks.append(new_task)
        save_tasks(tasks)
        st.sidebar.success("Task added successfully!")

# Edit an existing task
def edit_task(tasks):
    st.sidebar.subheader("Edit Task")
    task_names = [task['name'] for task in tasks]
    selected_task = st.sidebar.selectbox("Select Task", task_names)

    if selected_task:
        task = next(t for t in tasks if t['name'] == selected_task)
        task_name = st.sidebar.text_input("Task Name", value=task['name'])
        priority = st.sidebar.selectbox("Priority", ["High", "Medium", "Low"], index=["High", "Medium", "Low"].index(task['priority']))
        due_date = st.sidebar.date_input("Due Date", datetime.strptime(task['due_date'], '%Y-%m-%d'))
        recurring = st.sidebar.selectbox("Recurring", ["None", "Daily", "Weekly", "Monthly"], index=["None", "Daily", "Weekly", "Monthly"].index(task['recurring']))

        if st.sidebar.button("Update Task"):
            task['name'] = task_name
            task['priority'] = priority
            task['due_date'] = due_date.strftime('%Y-%m-%d')
            task['recurring'] = recurring
            save_tasks(tasks)
            st.sidebar.success("Task updated successfully!")

# Delete a task
def delete_task(tasks):
    st.sidebar.subheader("Delete Task")
    task_names = [task['name'] for task in tasks]
    selected_task = st.sidebar.selectbox("Select Task to Delete", task_names)

    if st.sidebar.button("Delete Task"):
        tasks = [task for task in tasks if task['name'] != selected_task]
        save_tasks(tasks)
        st.sidebar.success("Task deleted successfully!")
    
    return tasks

# Main app function
def main():
    st.set_page_config(page_title="KGI Task Manager", layout="wide")
    st.title("KGI Task Manager 📝")

    add_custom_css()

    # Load existing tasks
    tasks = load_tasks()

    # Sidebar options for task actions
    st.sidebar.title("Task Manager")
    add_task(tasks)
    edit_task(tasks)
    tasks = delete_task(tasks)

    # Handle recurring tasks
    tasks = handle_recurring_tasks(tasks)
    
    # Display tasks
    display_tasks(tasks)

    # Send notifications for upcoming tasks
    for task in tasks:
        due_date = datetime.strptime(task['due_date'], '%Y-%m-%d')
        if due_date - timedelta(days=1) <= datetime.now() <= due_date:
            send_notification(task['name'], task['due_date'])

if __name__ == "__main__":
    main()
