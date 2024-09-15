import streamlit as st
import json
from datetime import datetime
import os

TASK_DATA_PATH = 'data/tasks.json'

def load_tasks(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    return []

def save_tasks(file_path, tasks):
    with open(file_path, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    st.sidebar.subheader("Add Task")
    
    task_name = st.sidebar.text_input("Task Name", key="add_task_name")
    priority = st.sidebar.selectbox("Priority", ["High", "Medium", "Low"], key="add_task_priority")
    due_date = st.sidebar.date_input("Due Date", datetime.now().date(), key="add_task_due_date")
    recurring = st.sidebar.selectbox("Recurring", ["None", "Daily", "Weekly", "Monthly"], key="add_task_recurring")
    
    if st.sidebar.button("Add Task", key="add_task_button"):
        if task_name:
            tasks.append({
                'name': task_name,
                'priority': priority,
                'due_date': due_date.strftime('%Y-%m-%d'),
                'recurring': recurring,
                'completed': False
            })
            st.sidebar.success("Task added successfully!")
        else:
            st.sidebar.error("Task name cannot be empty!")

def edit_task(tasks):
    st.sidebar.subheader("Edit Task")
    
    selected_task = st.sidebar.selectbox("Select Task to Edit", [task['name'] for task in tasks], key="edit_task_selectbox")

    if selected_task:
        task = next(t for t in tasks if t['name'] == selected_task)
        task_name = st.sidebar.text_input("Task Name", value=task['name'], key="edit_task_name")
        priority = st.sidebar.selectbox("Priority", ["High", "Medium", "Low"], index=["High", "Medium", "Low"].index(task['priority']), key="edit_task_priority")
        due_date = st.sidebar.date_input("Due Date", datetime.strptime(task['due_date'], '%Y-%m-%d').date(), key="edit_task_due_date")
        recurring = st.sidebar.selectbox("Recurring", ["None", "Daily", "Weekly", "Monthly"], index=["None", "Daily", "Weekly", "Monthly"].index(task['recurring']), key="edit_task_recurring")
        
        if st.sidebar.button("Save Changes", key="edit_task_save"):
            task['name'] = task_name
            task['priority'] = priority
            task['due_date'] = due_date.strftime('%Y-%m-%d')
            task['recurring'] = recurring
            st.sidebar.success("Task updated successfully!")

def delete_task(tasks):
    st.sidebar.subheader("Delete Task")
    
    selected_task = st.sidebar.selectbox("Select Task to Delete", [task['name'] for task in tasks], key="delete_task_selectbox")

    if selected_task:
        if st.sidebar.button("Delete Task", key="delete_task_button"):
            tasks = [task for task in tasks if task['name'] != selected_task]
            st.sidebar.success("Task deleted successfully!")
    return tasks

def handle_recurring_tasks(tasks):
    updated_tasks = []
    today = datetime.now().date()

    for task in tasks:
        if task['recurring'] == "None":
            updated_tasks.append(task)
        else:
            due_date = datetime.strptime(task['due_date'], '%Y-%m-%d').date()
            if task['recurring'] == "Daily":
                new_due_date = today + timedelta(days=1)
            elif task['recurring'] == "Weekly":
                new_due_date = today + timedelta(weeks=1)
            elif task['recurring'] == "Monthly":
                new_due_date = today + timedelta(weeks=4)
                
            if new_due_date <= today:
                updated_tasks.append({
                    'name': task['name'],
                    'priority': task['priority'],
                    'due_date': new_due_date.strftime('%Y-%m-%d'),
                    'recurring': task['recurring'],
                    'completed': False
                })
    return updated_tasks

def filter_by_category_tag(tasks, category_tag):
    filtered_tasks = []
    for task in tasks:
        categories = task.get('categories', [])
        tags = task.get('tags', [])
        if category_tag in categories or category_tag in tags:
            filtered_tasks.append(task)
    return filtered_tasks

def send_notification(task_name, due_date):
    st.sidebar.write(f"Reminder: Task '{task_name}' is due on {due_date}")

