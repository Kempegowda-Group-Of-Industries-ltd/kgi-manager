import pandas as pd
import os
import streamlit as st
from datetime import datetime, timedelta

# Directory and file path
CALENDAR_FILE = 'data/calendar.csv'

# Load calendar events
def load_calendar():
    if not os.path.exists(CALENDAR_FILE):
        return pd.DataFrame(columns=["Event", "Start", "End"])
    return pd.read_csv(CALENDAR_FILE)

# Save a new event to calendar
def save_event(event_data):
    calendar = load_calendar()
    new_event = pd.DataFrame([event_data])
    calendar = pd.concat([calendar, new_event], ignore_index=True)
    calendar.to_csv(CALENDAR_FILE, index=False)

# Add event to calendar
def add_event_to_calendar(task_name, due_date):
    event = {
        'Event': task_name,
        'Start': due_date.isoformat(),
        'End': (due_date + timedelta(hours=1)).isoformat(),
    }
    save_event(event)
    st.success(f'Event created: {event.get("Event")}')

# View calendar
def view_calendar():
    calendar = load_calendar()
    st.write(calendar)
