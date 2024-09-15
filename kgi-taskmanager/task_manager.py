import json
from datetime import datetime

# Load tasks from file
def load_tasks(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(file_path, tasks):
    with open(file_path, 'w') as file:
        json.dump(tasks, file, indent=4)

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
            st.sidebar.success("Task updated successfully!")

# Delete a task
def delete_task(tasks):
    st.sidebar.subheader("Delete Task")
    task_names = [task['name'] for task in tasks]
    selected_task = st.sidebar.selectbox("Select Task to Delete", task_names)

    if st.sidebar.button("Delete Task"):
        tasks = [task for task in tasks if task['name'] != selected_task]
        st.sidebar.success("Task deleted successfully!")

    return tasks
