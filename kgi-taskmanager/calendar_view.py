import calendar
from datetime import datetime

def display_calendar(tasks):
    st.subheader("Calendar View")
    today = datetime.today()
    
    # Display current month
    month_calendar = calendar.monthcalendar(today.year, today.month)
    
    # Show tasks for the current month
    for week in month_calendar:
        st.write(" | ".join([str(day) if day > 0 else "" for day in week]))
        
    for task in tasks:
        st.write(f"Task: {task['name']} - Due: {task['due_date']}")
