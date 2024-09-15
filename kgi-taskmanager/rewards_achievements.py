import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def track_achievements(tasks):
    completed_tasks = sum(1 for task in tasks if task['completed'])
    
    # Track achievements
    st.subheader("Achievements")
    
    # Define achievements
    achievements = {
        "Task Master": 10,
        "Productivity King": 20,
        "Super Achiever": 30
    }

    # Determine current achievement
    current_achievement = None
    for achievement, threshold in sorted(achievements.items(), key=lambda x: x[1], reverse=True):
        if completed_tasks > threshold:
            current_achievement = achievement
            break

    if current_achievement:
        st.write(f"Achievement Unlocked: {current_achievement}")
    else:
        st.write("No new achievements unlocked.")

    # Display achievements progress
    st.subheader("Achievements Progress")
    achievement_names = list(achievements.keys())
    thresholds = list(achievements.values())
    progress = [min(completed_tasks, threshold) for threshold in thresholds]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=achievement_names, y=progress, ax=ax)
    ax.set_title("Achievements Progress")
    ax.set_xlabel("Achievements")
    ax.set_ylabel("Tasks Completed")
    st.pyplot(fig)

    # Pie chart of achievement progress
    if completed_tasks > 0:
        fig, ax = plt.subplots()
        labels = list(achievements.keys())
        sizes = [min(completed_tasks, threshold) for threshold in thresholds]
        sizes.append(completed_tasks - sum(sizes))  # Remaining tasks

        ax.pie(sizes, labels=labels + ["Remaining"], autopct='%1.1f%%', startangle=140)
        ax.set_title("Achievement Distribution")
        st.pyplot(fig)
    else:
        st.write("No tasks completed yet.")
