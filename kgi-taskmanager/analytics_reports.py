import streamlit as st  # Import Streamlit
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import io

def generate_report(tasks):
    st.subheader("Analytics Report")

    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task['completed'])
    
    # Avoid division by zero
    completion_rate = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0

    st.write(f"Total Tasks: {total_tasks}")
    st.write(f"Completed Tasks: {completed_tasks}")
    st.write(f"Completion Rate: {completion_rate:.2f}%")

    # Breakdown by Priority
    priority_counts = {'High': 0, 'Medium': 0, 'Low': 0}
    for task in tasks:
        priority_counts[task['priority']] += 1

    # Plot Breakdown by Priority
    fig, ax = plt.subplots()
    sns.barplot(x=list(priority_counts.keys()), y=list(priority_counts.values()), ax=ax)
    ax.set_title("Breakdown by Priority")
    ax.set_xlabel("Priority")
    ax.set_ylabel("Number of Tasks")
    st.pyplot(fig)

    # Tasks Due in the Next 7 Days
    today = datetime.now().date()
    upcoming_tasks = [task for task in tasks if not task['completed'] and datetime.strptime(task['due_date'], '%Y-%m-%d').date() <= today + timedelta(days=7)]
    
    st.write(f"Tasks Due in the Next 7 Days: {len(upcoming_tasks)}")
    for task in upcoming_tasks:
        st.write(f"- {task['name']} (Due: {task['due_date']})")

    # Number of Tasks per Category/Tag
    category_tag_counts = {}
    for task in tasks:
        categories = task.get('categories', [])
        tags = task.get('tags', [])
        for cat in categories:
            category_tag_counts[cat] = category_tag_counts.get(cat, 0) + 1
        for tag in tags:
            category_tag_counts[tag] = category_tag_counts.get(tag, 0) + 1

    # Plot Number of Tasks per Category/Tag
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=list(category_tag_counts.keys()), y=list(category_tag_counts.values()), ax=ax)
    ax.set_title("Number of Tasks per Category/Tag")
    ax.set_xlabel("Category/Tag")
    ax.set_ylabel("Number of Tasks")
    plt.xticks(rotation=45, ha="right")
    st.pyplot(fig)

    # Plot Tasks Due in the Next 7 Days (Pie Chart)
    upcoming_due_dates = [datetime.strptime(task['due_date'], '%Y-%m-%d').date() for task in upcoming_tasks]
    due_dates_count = {date: upcoming_due_dates.count(date) for date in set(upcoming_due_dates)}

    fig, ax = plt.subplots()
    ax.pie(due_dates_count.values(), labels=[str(date) for date in due_dates_count.keys()], autopct='%1.1f%%', startangle=140)
    ax.set_title("Distribution of Tasks Due in the Next 7 Days")
    st.pyplot(fig)


import streamlit as st  # Import Streamlit
from datetime import datetime, timedelta

def generate_report(tasks):
    st.subheader("Analytics Report")

    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task['completed'])
    
    # Avoid division by zero
    completion_rate = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0

    st.write(f"Total Tasks: {total_tasks}")
    st.write(f"Completed Tasks: {completed_tasks}")
    st.write(f"Completion Rate: {completion_rate:.2f}%")

    # Breakdown by Priority
    priority_counts = {'High': 0, 'Medium': 0, 'Low': 0}
    for task in tasks:
        priority_counts[task['priority']] += 1

    st.write("Breakdown by Priority:")
    for priority, count in priority_counts.items():
        st.write(f"{priority}: {count} tasks")

    # Tasks Due in the Next 7 Days
    today = datetime.now().date()
    upcoming_tasks = [task for task in tasks if not task['completed'] and datetime.strptime(task['due_date'], '%Y-%m-%d').date() <= today + timedelta(days=7)]
    
    st.write(f"Tasks Due in the Next 7 Days: {len(upcoming_tasks)}")
    for task in upcoming_tasks:
        st.write(f"- {task['name']} (Due: {task['due_date']})")

    # Number of Tasks per Category/Tag
    category_tag_counts = {}
    for task in tasks:
        categories = task.get('categories', [])
        tags = task.get('tags', [])
        for cat in categories:
            category_tag_counts[cat] = category_tag_counts.get(cat, 0) + 1
        for tag in tags:
            category_tag_counts[tag] = category_tag_counts.get(tag, 0) + 1
    
    st.write("Number of Tasks per Category/Tag:")
    for category_tag, count in category_tag_counts.items():
        st.write(f"{category_tag}: {count} tasks")
