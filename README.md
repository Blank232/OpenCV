# Hand Gesture Volume Control

## Overview
This project allows users to control system volume using hand gestures detected via a webcam. It utilizes OpenCV for real-time hand tracking, Mediapipe for hand landmark detection, and Pycaw for audio control.

## Features
- Real-time hand tracking using OpenCV and Mediapipe
- Adjusts system volume based on finger distance
- Displays volume percentage and visual feedback on screen
- Dynamic FPS display

## Requirements
Ensure you have the following dependencies installed before running the script:

```sh
pip install opencv-python mediapipe numpy comtypes pycaw
```

## Usage
1. Run the script:
   ```sh
   python hand_gesture_volume.py
   ```
2. Make sure your webcam is on.
3. Adjust the volume using your thumb and index finger:
   - Bring them closer to decrease volume.
   - Move them apart to increase volume.
4. The volume percentage and a visual bar will be displayed on the screen.

## How It Works
- The script initializes the webcam and sets up hand tracking using a custom module `HandTrackingModule`.
- It detects the thumb (landmark 4) and index finger (landmark 8) positions.
- The distance between these fingers is mapped to the system's volume range using `numpy.interp()`.
- The volume is then updated using `SetMasterVolumeLevel()` from the Pycaw library.

## Demo
![Hand Gesture Volume Control](https://your-demo-image-link.png)

## Known Issues
- Ensure `HandTrackingModule.py` is present in the same directory.
- Hand tracking accuracy may vary in different lighting conditions.

## Author
Ishir Srivats
