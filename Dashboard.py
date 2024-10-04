import streamlit as st
import random
import os

st.set_page_config(layout="wide")

# List of video files and their corresponding camera titles
video_files = [
    os.path.join("processed_videos", "video1_compressed.mp4"),
    os.path.join("processed_videos", "video2_compressed.mp4"),
    os.path.join("processed_videos", "pedestrian_hit.mp4"),
    os.path.join("processed_videos", "video5_compressed.mp4"),
    os.path.join("processed_videos", "video6_compressed.mp4"),
    os.path.join("videos", "video1.mp4"),
    os.path.join("videos", "video2.mp4"),
    os.path.join("videos", "video4.mp4"),
    os.path.join("videos", "video5.mp4"),
    os.path.join("videos", "video6.mp4"),
]

# Function to generate random locations
def generate_random_location():
    locations = [
        ("New York", (40.7128, -74.0060)),
        ("Los Angeles", (34.0522, -118.2437)),
        ("Chicago", (41.8781, -87.6298)),
        ("Houston", (29.7604, -95.3698)),
        ("Phoenix", (33.4484, -112.0740)),
        ("Philadelphia", (39.9526, -75.1652)),
        ("San Antonio", (29.4241, -98.4936)),
        ("San Diego", (32.7157, -117.1611)),
        ("Dallas", (32.7767, -96.7970)),
        ("San Jose", (37.3382, -121.8863))
    ]
    return random.choice(locations)

# Create a log file with random tags and locations
def log_video_data(video):
    tag = random.choice([0, 1])
    location_name, location_coordinates = generate_random_location()
    with open(os.path.join(os.getcwd(), "video_log.txt"), "a") as f:
        f.write(f"{video}, {tag}, {location_name}, ({location_coordinates[0]}, {location_coordinates[1]})\n")

# Display videos in rows of three
num_columns = 3

# Create columns once for the entire video list
cols = st.columns(num_columns)

for index, video in enumerate(video_files):
    # Calculate the column index for the current video
    col_index = index % num_columns
    
    # Display the video with autoplay and looping
    with cols[col_index]:
        st.subheader(f"Video {index + 1}")
        st.video(video, format="video/mp4", autoplay=True, muted=True)  # Video autoplaying muted
        
        # Log video data when displayed
        log_video_data(video)
        
        # Display the generated tag and location
        tag = random.choice([0, 1])  # Simulate tag generation for demonstration
        location_name, location_coordinates = generate_random_location()
        st.write(f"**Tag:** {tag}")
        st.write(f"**Location:** {location_name}")
        st.write(f"**Coordinates:** {location_coordinates}")
        
        st.markdown("---")  # Add a horizontal line for separation
