# color_detection.py

import cv2
import numpy as np

def detect_color(region, color_ranges):
    """Detect the dominant color in a given region."""
    hsv_region = cv2.cvtColor(region, cv2.COLOR_BGR2HSV)
    max_score = 0
    detected_color = None
    for color, (lower, upper) in color_ranges.items():
        lower = np.array(lower)
        upper = np.array(upper)
        color_mask = cv2.inRange(hsv_region, lower, upper)
        score = np.sum(color_mask)  # Summing the mask's white pixel values gives an idea of dominance
        if score > max_score:
            max_score = score
            detected_color = color
    return detected_color
