# config.py
import os
'''choose the color ranges that you prefer'''
''''
# Define refined color ranges in HSV space for Rubik's Cube colors
color_ranges = {
    "orange": ([5, 150, 150], [15, 255, 255]),
    "red": ([170, 150, 150], [180, 255, 255]),
    "yellow": ([20, 100, 100], [40, 255, 255]),
    "white": ([0, 0, 200], [180, 30, 255]),
    "green": ([35, 100, 100], [75, 255, 255]),
    "blue": ([90, 100, 100], [130, 255, 255])
}
'''


color_ranges = {
    "orange": ([5, 120, 100], [15, 255, 255]),
    "red": ([160, 150, 130], [180, 255, 255]),
    "yellow": ([20, 100, 100], [40, 255, 255]),
    "white": ([0, 0, 180], [180, 30, 255]),
    "green": ([40, 40, 40], [70, 255, 255]),
    "blue": ([95, 100, 100], [135, 255, 255])
}


"""
color_ranges = {
    "orange": ([5, 150, 150], [15, 255, 255]),
    "red": ([170, 150, 150], [180, 255, 255]),
    "yellow": ([20, 100, 100], [40, 255, 255]),
    "white": ([0, 0, 200], [180, 30, 255]),
    "green": ([35, 100, 100], [75, 255, 255]),
    "blue": ([90, 100, 100], [130, 255, 255])
}
"""

# Initialize requided files
os.makedirs('assets/config/', exist_ok=True)
os.makedirs('assets/images/', exist_ok=True)