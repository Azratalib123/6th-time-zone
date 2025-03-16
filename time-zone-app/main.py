# Import required libraries
import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

# List of available time zones
TIME_ZONES = [
    "UTC",
    "Asia/Karachi",
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "America/Los_Angeles",
    "Europe/Berlin",
    "Asia/Dubai",
    "Asia/Kolkata",
]

# App title
st.title("🌍 Time Zone Converter")

# Multi-select dropdown for choosing time zones
selected_timezone = st.multiselect(
    "Choose Timezones to Display", TIME_ZONES, default=["UTC", "Asia/Karachi"]
)

# Display current time for selected time zones
st.subheader("⏰ Current Time in Selected Timezones")
for tz in selected_timezone:
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    st.write(f"**{tz}** → {current_time}")

# Section for time conversion
st.subheader("🔄 Convert Time Between Timezones")

# Time input field with current time as default
input_time = st.time_input("Select Time", value=datetime.now().time())

# Dropdowns for selecting source and target time zones
from_tz = st.selectbox("Convert From", TIME_ZONES, index=0)
to_tz = st.selectbox("Convert To", TIME_ZONES, index=1)

# Convert time on button click
if st.button("🔄 Convert"):
    dt = datetime.combine(datetime.today(), input_time, tzinfo=ZoneInfo(from_tz))
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    st.info(f"📍 **Time in {to_tz}:** {converted_time}")
