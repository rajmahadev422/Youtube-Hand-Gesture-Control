
# 👋Hand Gesture Control

A real-time hand gesture recognition system that uses MediaPipe to detect hand gestures and control applications via keyboard simulation.

## Features

- Real-time hand gesture detection using MediaPipe
- Gesture-to-keyboard mapping for application control
- Support for multiple gestures: Thumb Up, Thumb Down, Closed Fist, Open Palm
- Pause/Resume functionality with Closed Fist and Open Palm gestures

## Installation

1. Clone or download this project

2. Install dependencies:

  ```bash
  pip install -r requirements.txt
  ```

## Prerequisites

- Python 3.8+
- Webcam
- MediaPipe gesture recognizer model (`gesture_recognizer.task`)

## Usage

Run the application:

  ```bash
  python main.py
  ```

Press `q` to exit the application.

## Gesture Mappings

| Gesture | Action |
| --------- | -------- |
| Thumb Up | Press `l` (forward) |
| Thumb Down | Press `j` (backward) |
| Closed Fist | Press `k` (pause) |
| Open Palm | Press `k` (resume) |

## How It Works

1. Captures video from webcam
2. Processes frames with MediaPipe gesture recognizer
3. Detects hand gestures in real-time
4. Simulates keyboard presses based on recognized gestures
5. Displays current gesture on video feed

## Requirements

See `requirements.txt` for dependencies.
