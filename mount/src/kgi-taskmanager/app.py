import streamlit as st
import pandas as pd
from datetime import datetime
from task_manager import load_tasks, save_task, update_task, delete_task
from local_calendar import view_calendar, add_event_to_calendar

def main():
    st.set_page_config(page_title="KGI Task Manager", layout="wide")
    st.title("KGI Task Manager")

    menu = ["Add Task", "View Tasks", "Update Task", "Delete Task", "Calendar"]
    choice = st.sidebar.selectbox("Select an option", menu)

    if choice == "Add Task":
        st.subheader("Add New Task")
        name = st.text_input("Task Name")
        if st.button("Add Task"):
            st.write(f"Task '{name}' added!")  # For testing

    elif choice == "View Tasks":
        st.subheader("View All Tasks")
        tasks = load_tasks()
        st.write(tasks)

    elif choice == "Update Task":
        st.subheader("Update Existing Task")
        name = st.text_input("Task Name to Update")
        if st.button("Update Task"):
            st.write(f"Updating task '{name}'")  # For testing

    elif choice == "Delete Task":
        st.subheader("Delete Task")
        name = st.text_input("Task Name to Delete")
        if st.button("Delete Task"):
            st.write(f"Deleting task '{name}'")  # For testing

    elif choice == "Calendar":
        st.subheader("Local Calendar")
        view_calendar()

if __name__ == "__main__":
    main()
