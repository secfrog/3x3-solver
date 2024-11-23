# main.py

import cv2
import numpy as np
import time
from config.config import color_ranges                                                         # config.py
from detection.color_detection import detect_color                                                # color_detection.py
from solver.face_state import initialize_face_state, update_face_state, display_face_state     # Cube state.py
from utils.utils import initialize_video_capture
from solver.kociemba_algo import solve


def f(c):
    # Initialize the Rubik's Cube state
    face_state = initialize_face_state()

    # Initialize video capture
    cap = initialize_video_capture()
    if cap is None:
        exit()


    ret, image = cap.read()

    # Convert to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # Initialize the combined mask
    combined_mask = np.zeros_like(hsv_image[:, :, 0])
    # Create and combine masks for all defined colors
    for color, (lower, upper) in color_ranges.items():
        lower = np.array(lower)
        upper = np.array(upper)
        color_mask = cv2.inRange(hsv_image, lower, upper)
        combined_mask = cv2.bitwise_or(combined_mask, color_mask)
    # Apply morphological operations to clean the mask (remove small noise) [chatgpt]
    kernel = np.ones((5, 5), np.uint8)
    combined_mask = cv2.morphologyEx(combined_mask, cv2.MORPH_CLOSE, kernel)
    combined_mask = cv2.morphologyEx(combined_mask, cv2.MORPH_OPEN, kernel)
    # Find contours in the combined mask
    contours, _ = cv2.findContours(combined_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Draw bounding boxes around detected areas
    result = cv2.bitwise_and(image, image, mask=combined_mask)
    grid_size = 3
    for contour in contours:
        if cv2.contourArea(contour) > 500:  # Filter out small areas
            x, y, w, h = cv2.boundingRect(contour)
            aspect_ratio = w / float(h)
            if 0.8 < aspect_ratio < 1.2:
                cv2.rectangle(result, (x, y), (x + w, y + h), (0, 255, 0), 2)
                isolated_region = image[y:y + h, x:x + w]
                height, width = isolated_region.shape[:2]
                square_height = height // grid_size
                square_width = width // grid_size
                cv2.imwrite(f'assets/images/{c}isolated_region.jpg', isolated_region); print(' iso , done ')
                for i in range(grid_size):
                    for j in range(grid_size):
                        start_x = j * square_width
                        start_y = i * square_height
                        grid_square = isolated_region[start_y:start_y + square_height, start_x:start_x + square_width]
                        color = detect_color(grid_square, color_ranges)
                        update_face_state(face_state, i, j, color)
    # Display the result with bounding boxes
    cv2.imwrite(f'assets/images/{c}Masked_Image.jpg', result); print('main window, done')
    # Display the Rubik's Cube state
    display_face_state(face_state)

    # Release the capture object and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()


color_list = ['yellow', 'blue', 'orange', 'white', 'green', 'red']
guide_user = ["^\n|  - - >\n|", "< - -", "^\n|\n|", "| < - -\n|\nv", "< - - ", "Done"]
for i in range(6):
    c = color_list[i]

    with open('assets/config/c.txt', 'w') as cr:
        cr.write(f'{c}')
        
    time.sleep(3)
    f(c)
    print('face captured')
    if i!=5:
        print("next")
    print(guide_user[i])
    
# check solver/kociemba_algo
solve()