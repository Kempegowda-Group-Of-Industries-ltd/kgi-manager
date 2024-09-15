import streamlit as st
from task_manager import load_tasks, save_tasks, add_task, edit_task, delete_task
from recurring_tasks import handle_recurring_tasks
from categories_tags import filter_by_category_tag
from calendar_view import display_calendar
from analytics_reports import generate_report
from rewards_achievements import track_achievements
from notifications import send_notification
import os

# Define the path to the tasks data file
TASK_DATA_PATH = os.path.join("data", "tasks.json")

import streamlit as st

# Load the CSS file
def load_css():
    with open("templates/dark_mode.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def main():
    # Load CSS
    load_css()

    st.title("KGI Task Manager App")
    
    # Your app code here
    app_mode = st.sidebar.selectbox("Select App Mode", ["Task Manager", "Calendar", "Analytics", "Rewards"])

    if app_mode == "Task Manager":
        st.sidebar.subheader("Task Operations")
        # Call your functions for adding, editing, deleting tasks, etc.

    elif app_mode == "Calendar":
        # Call your function to display calendar view
        pass

    elif app_mode == "Analytics":
        # Call your function to generate report
        pass

    elif app_mode == "Rewards":
        # Call your function for tracking achievements
        pass

if __name__ == "__main__":
    main()

def main():
    # Ensure the data directory exists
    if not os.path.exists("data"):
        os.makedirs("data")

    # Load tasks from file
    tasks = load_tasks(TASK_DATA_PATH)
    
    st.set_page_config(page_title="KGI Task Manager", layout="wide")
    st.title("KGI Task Manager 📝")
    
    # Sidebar navigation
    st.sidebar.title("Navigation")
    app_mode = st.sidebar.selectbox("Select Mode", ["Task Manager", "Calendar", "Analytics", "Rewards", "Settings"])

    # Task Manager View
    if app_mode == "Task Manager":
        st.sidebar.subheader("Task Operations")
        add_task(tasks)
        edit_task(tasks)
        tasks = delete_task(tasks)
        tasks = handle_recurring_tasks(tasks)
        save_tasks(TASK_DATA_PATH, tasks)

        # Task Categories/Tags Filtering
        if st.sidebar.checkbox("Filter by Category/Tag"):
            category_tag = st.sidebar.text_input("Enter Category/Tag")
            tasks = filter_by_category_tag(tasks, category_tag)

        # Display Tasks
        for task in tasks:
            st.write(f"Task: {task['name']} - Priority: {task['priority']} - Due: {task['due_date']}")
            if task['priority'] == "High":
                send_notification(task['name'], task['due_date'])

    # Calendar View
    elif app_mode == "Calendar":
        display_calendar(tasks)

    # Analytics View
    elif app_mode == "Analytics":
        st.subheader("Task Analytics")
        generate_report(tasks)

    # Rewards & Achievements View
    elif app_mode == "Rewards":
        st.subheader("Rewards & Achievements")
        track_achievements(tasks)

    # Settings (Dark Mode, etc.)
    elif app_mode == "Settings":
        theme = st.sidebar.selectbox("Choose Theme", ["Light", "Dark"])
        if theme == "Dark":
            st.markdown('<link href="templates/dark_mode.css" rel="stylesheet">', unsafe_allow_html=True)
        else:
            st.markdown('<link href="templates/base.css" rel="stylesheet">', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
