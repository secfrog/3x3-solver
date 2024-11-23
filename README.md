# 3x3-Solver

A Rubik's Cube solver tool that uses computer vision to detect cube faces and the Kociemba algorithm to find the solution.

## Prerequisites

- **Python** is required (Python 3.x is recommended).
- You will also need the following Python packages:
  - `opencv-contrib-python` (or `opencv-python` for a lighter version)
  - `kociemba` (for the Kociemba algorithm)

## Installation

To install the required dependencies, run the following commands in your command prompt:

```bash
pip install opencv-contrib-python
# OR, for a lighter version:
pip install opencv-python
pip install kociemba
```

# Project Structure

Here's a breakdown of the project structure:
```
3x3-solver/
│
├── assets/                    # Examples of the tool output
│   ├── config/                # Configuration files
│   │   ├── c.txt
│   │   └── Cube.txt
│   ├── images/                # Captured cube images
│   └── ...
│
├── config/                    # Configuration scripts
│   └── config.py
│
├── detection/                 # Cube face detection scripts
│   └── color_detection.py
│
├── solver/                    # Rubik's Cube solving scripts
│   ├── face_state.py
│   └── kociemba_algo.py
│
├── tests/                     # Unit tests
│   └── state_test.py
│
├── utils/                     # Utility functions
│   └── utils.py
│
├── main.py                    # Main entry point to run the solver
├── requirements.txt           # List of required packages
└── test_camera.py             # Camera testing script
```

# Usage
## Camera setup
Before running the solver, you need to test your camera to ensure that it correctly detects the cube's faces and colors. You can do this by running the following script:
`python test_camera.py`

The script will guide you through testing the detection of the cube's faces. Ensure that each face is detected correctly (matching the colors with the ones you set in the config.py).

## Cube Orientation
The solver relies on specific color assignments for the cube faces. Ensure that the cube is oriented as follows:

   - Yellow: Top face (U)
   - Blue: Right face (R)
   - Orange: Front face (F)
   - White: Bottom face (D)
   - Green: Left face (L)
   - Red: Back face (B)

## Capturing Cube Faces
Once your camera is properly configured, run the main.py script to start the process of capturing the six faces of the cube. The program will guide you through capturing the faces in the following order:

  - U - Top face (Yellow)
  - R - Right face (Blue)
  - F - Front face (Orange)
  - D - Bottom face (White)
  - L - Left face (Green)
  - B - Back face (Red)

 For each face, make sure the camera captures the face in the correct orientation. After each face is captured, you will see a prompt to rotate the cube to the next face.

## Running the Solver
After all six faces are captured, the program will use the Kociemba algorithm to solve the cube and display the solution steps.

# Additional Information
* The project uses OpenCV to detect the colors and orientations of the cube's faces.
* The Kociemba algorithm is used to compute the solution to the scrambled cube.
* If you encounter any issues with cube face detection, ensure your lighting conditions are good and the camera can clearly distinguish the cube's faces.

# Contributing
Feel free to fork this repository, create issues, and submit pull requests. Contributions are welcome!
