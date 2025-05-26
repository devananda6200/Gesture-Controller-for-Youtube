# Gesture-Controller-for-Youtube
This project uses a webcam and computer vision to control YouTube playback with hand gestures. By detecting specific finger combinations using MediaPipe and OpenCV, it maps gestures like thumbs up, fist, or single-finger raises to YouTube controls like play, pause, forward, and rewind — all hands-free. 

# 🎥 YouTube Gesture Controller using Python & MediaPipe

Control YouTube videos using just your hand gestures — no mouse or keyboard required!

https://github.com/devananda6200/Gesture-Controller-for-Youtube

---

## ✨ Features

- 👍 **Thumb Up**: Play video  
- ✊ **Fist**: Pause video  
- 👉 **Index Finger Up**: Forward 10 seconds  
- 🖕 **Middle Finger Up**: Backward 10 seconds  
- 🤖 Real-time hand tracking using MediaPipe  
- 🖥️ Works directly in YouTube browser tab

---

## 📸 Demo

[https://youtu.be/OaB2oBqhvmM](https://youtu.be/OaB2oBqhvmM) 


---

## 🧠 How It Works

- Uses **MediaPipe** to detect hand landmarks.
- Identifies which fingers are raised.
- Sends keypresses (`k`, `j`, `l`) using **pyautogui** to control YouTube.
- Automatically activates your YouTube browser tab.

---
## 📁 Project Structure

- `handtracking.py`:  
  A utility module that wraps MediaPipe's hand detection and landmark drawing functionality. This keeps your code modular and reusable.

- `gesture_control.py`:  
  The core logic for recognizing hand gestures based on finger positions and triggering the appropriate keyboard shortcuts using PyAutoGUI.

- `main.py`:  
  The main entry point that integrates video capture, hand tracking, and gesture recognition. It also displays the live webcam feed with gesture labels.

---

## ▶️ How to Run

### 1. 🛠 Install Dependencies

Make sure you have Python 3.10 installed. Then install the required libraries:

```bash
pip install opencv-python mediapipe pyautogui pygetwindow
python gesture_control.py
