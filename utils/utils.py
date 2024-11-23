# utils.py

import cv2

def initialize_video_capture():
    """Initialize the video capture object."""
    cap = cv2.VideoCapture(0) # Default camera
    if not cap.isOpened():
        print("Error: Could not open video stream.")
        return None
    return cap
