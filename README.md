# Automated Traffic Incident Detection System

## Introduction

### Traffic Congestion
Rapid urbanization has led to a significant increase in the number of vehicles on roads, causing severe congestion. Urban areas are seeing record levels of traffic, negatively impacting productivity and quality of life.

### Accidents and Road Rage
Accidents are a leading cause of traffic jams and contribute to increased air pollution. Road rage incidents are becoming more common, posing threats to public safety.

### Monitoring Limitations
Manual monitoring of all CCTV feeds is impractical due to the sheer volume of footage. The lack of timely reporting leads to delays in responding to incidents, which further worsens traffic situations.

## Problem Statement
Traffic congestion and road accidents are major global issues, leading to delays and increased carbon footprints. Current monitoring methods are inadequate for real-time incident detection. We propose a solution using CCTV footage to automatically detect accidents and road rage, capturing essential details like vehicle number plates for law enforcement. This system aims to enhance accident investigations and improve road safety.

## Proposed Solution

### Automated Accident and Road Rage Detection
An AI-based system integrated with existing CCTV networks to analyze footage for accidents and road rage. The system uses deep learning techniques to recognize patterns related to accidents or aggressive driving behaviors.

### Number Plate Recognition
When incidents are detected, number plate recognition captures the vehicle details, providing valuable information to law enforcement for follow-up.

### Real-Time Alerts
The system sends real-time alerts to authorities for quicker response. Automated notification systems can reduce response time and help clear congestion faster.

## About the Dataset
The Proposed Highway Incidents Detection Dataset (HWID12) is the first dataset designed to advance video action recognition for real-time highway incident detection, addressing a significant challenge in intelligent transportation systems. Currently, the absence of such datasets has hindered the application of recent breakthroughs in video action classification. HWID12 includes over 2,780 video clips, each 3 to 8 seconds long, capturing moments before, during, and after incidents. These clips were manually segmented from accident compilation videos sourced from YouTube and other platforms.

## Conclusion

### Summary
Our solution provides an AI-driven approach to detect accidents and road rage incidents using CCTV footage. By automating monitoring and response, it significantly enhances public safety and reduces traffic congestion. The system also helps reduce the carbon footprint, contributing to environmental sustainability. Ultimately, the solution aims to support law enforcement, ensure faster emergency response, and improve the overall efficiency of urban traffic management.

### Call to Action
We believe this solution can significantly impact urban mobility and road safety. We are open to collaboration to make our roads safer and more efficient.

## Download Pretrained Weights

To use the pretrained model, you need to download the weights file and place it in the `weights/` folder in the root directory of the project.

### Instructions:

1. Click on the following link to download the weights file:
   [Download Weights from Google Drive](https://drive.google.com/file/d/18jZXNuJsQEZfHaDanaL3iXIWPAXBr17T/view?usp=sharing)

2. Create a folder named `weights` in the root directory of this project if it doesn't already exist.

3. Move the downloaded `accident.pt` file into the `weights/` folder.

   ```bash
   mkdir -p weights
   mv path_to_downloaded_weights/accident.pt weights/
   ```
