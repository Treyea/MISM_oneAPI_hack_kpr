import streamlit as st
import os

st.set_page_config(layout="wide")

st.title("Alerts")

# Function to read the log file and return its content
def get_logs():
    logs = []
    log_file_path = os.path.join(os.getcwd(), "video_log.txt")  # Make the path OS-independent
    try:
        with open(log_file_path, "r") as f:
            for line in f:
                logs.append(line.strip())
    except FileNotFoundError:
        logs.append("No logs available yet.")
    return logs

# Display logs in a card-style format
logs = get_logs()

# Check if logs are empty for debugging
if logs:
    st.write("Logs found:")
    st.write(logs)
else:
    st.write("No logs available yet.")

# Create a list to hold video information
video_data = []

# Create video data for each log
for log in logs:
    video_info = log.split(", ")
    if len(video_info) == 4:  # Now we expect 4 items: video, tag, location name, location coordinates
        video, tag, location_name, coordinates = video_info
        video_data.append((video, tag, location_name, coordinates))

# Initialize session state variable if it doesn't exist
if 'refresh' not in st.session_state:
    st.session_state.refresh = 0

# Function to increment the state
def refresh_state():
    st.session_state.refresh += 1

# Refresh button
st.button('Refresh Data', on_click=refresh_state)

# Display the videos in rows of three
for i in range(0, len(video_data), 3):
    cols = st.columns(3)  # Create three columns
    for j in range(3):
        if i + j < len(video_data):
            video, tag, location_name, coordinates = video_data[i + j]
            # Use os.path.join to create a platform-independent path for the video
            video_path = os.path.join(os.getcwd(), video.replace("Video: ", ""))
            with cols[j]:
                # Create a card-like layout using Streamlit components
                st.subheader(video_path)
                try:
                    # Using a unique key for each video
                    st.video(video_path, format="video/mp4", autoplay=True, muted=True, key=f"video_{i + j}")
                except Exception as e:
                    st.write(f"Error loading video: {e}")
                st.write(f"**Tag:** {tag}")
                st.write(f"**Location:** {location_name}")
                st.write(f"**Coordinates:** {coordinates}")
                st.markdown("---")
