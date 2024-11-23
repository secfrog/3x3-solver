# face_state.py

import cv2
import numpy as np

def initialize_face_state(size=3):
    """Initialize a 3x3 grid to represent the Rubik's Cube state."""
    return [["" for _ in range(size)] for _ in range(size)]

def update_face_state(face_state, row, col, color):
    """Update a specific square on the Rubik's Cube."""
    face_state[row][col] = color

def display_face_state(face_state):
    """Display the Rubik's Cube state in a graphical format."""
    square_size = 100  # Size of each square in the grid (in pixels)
    grid_size = len(face_state)
    face_display = np.zeros((grid_size * square_size, grid_size * square_size, 3), dtype=np.uint8)  # Blank image for visualization
    
    for i in range(grid_size):
        for j in range(grid_size):
            color_name = face_state[i][j]
            color_bgr = (0, 0, 0)  # Default to black (if no color detected)
            if color_name == "orange":
                color_bgr = (0, 165, 255)
            elif color_name == "red":
                color_bgr = (0, 0, 255)
            elif color_name == "yellow":
                color_bgr = (0, 255, 255)
            elif color_name == "white":
                color_bgr = (255, 255, 255)
            elif color_name == "green":
                color_bgr = (0, 255, 0)
            elif color_name == "blue":
                color_bgr = (255, 0, 0)

            # Draw the grid square with the detected color
            cv2.rectangle(face_display, 
                          (j * square_size, i * square_size),
                          ((j + 1) * square_size, (i + 1) * square_size),
                          color_bgr, -1)

    cv2.imshow('face_State', face_display)