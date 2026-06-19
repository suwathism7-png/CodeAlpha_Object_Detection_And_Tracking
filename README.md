# Object Detection and Tracking with YOLOv8

This project is part of my **Artificial Intelligence Internship** at **CodeAlpha**. It demonstrates a real-time computer vision pipeline capable of detecting everyday objects and tracking them continuously across video frames using a webcam feed.

## Features
* **Real-Time Detection:** Uses a pre-trained YOLOv8 (nano) model to identify 80+ distinct object classes out of the box.
* **Persistent Object Tracking:** Integrates ByteTrack/SORT tracking algorithms to assign unique, consistent IDs to detected objects as they move.
* **Live Annotation:** Automatically overlays bounding boxes, confidence scores, and tracking labels onto the video stream.

## Repository Structure
* `app.py` - The core Python script managing the webcam stream and AI pipeline.
* `requirements.txt` - The list of necessary Python package dependencies.
* `README.md` - Documentation for project setup and execution.

## Getting Started

### Prerequisites
Make sure you have Python 3.8 or higher installed on your machine.

### Installation

1. Clone this repository to your local system:
   ```bash
   git clone [https://github.com/YOUR_GITHUB_USERNAME/CodeAlpha_ProjectName.git](https://github.com/YOUR_GITHUB_USERNAME/CodeAlpha_ProjectName.git)
   cd CodeAlpha_ProjectName