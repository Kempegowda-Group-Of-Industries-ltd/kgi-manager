import streamlit as st
from datetime import datetime
import calendar

def display_calendar(tasks):
    st.subheader("Calendar View")
    
    today = datetime.today()
    year = today.year
    month = today.month

    # Sidebar to select year and month
    st.sidebar.subheader("Select Year and Month")
    year = st.sidebar.slider("Year", min_value=2020, max_value=2100, value=year)
    month = st.sidebar.slider("Month", min_value=1, max_value=12, value=month)

    # Display the calendar for the selected month and year
    cal = calendar.Calendar()
    month_days = cal.monthdayscalendar(year, month)
    month_name = calendar.month_name[month]
    
    st.write(f"### {month_name} {year}")

    # Create a DataFrame to hold calendar data
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    
    # Display the days of the week
    with col1:
        st.write(days_of_week[0])
    with col2:
        st.write(days_of_week[1])
    with col3:
        st.write(days_of_week[2])
    with col4:
        st.write(days_of_week[3])
    with col5:
        st.write(days_of_week[4])
    with col6:
        st.write(days_of_week[5])
    with col7:
        st.write(days_of_week[6])
    
    # Display the calendar days
    for week in month_days:
        with st.container():
            for i, day in enumerate(week):
                if day == 0:
                    st.write("")
                else:
                    day_str = f"{day:2d}"
                    st.write(day_str)
