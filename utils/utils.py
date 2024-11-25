# utils.py

import cv2

def initialize_video_capture(ip_camera_url=None):

    if ip_camera_url:
        cap = cv2.VideoCapture(ip_camera_url)  # Use the IP camera stream
    else:
        cap = cv2.VideoCapture(0)  # Default camera

    if not cap.isOpened():
        print("Error: Could not open video stream.")
        return None
    return cap
