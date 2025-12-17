#🖱️ GestureMouse – Virtual Mouse Using Hand Gesture Recognition


**📌 Project Overview**

GestureMouse is a virtual mouse control system that allows users to control the computer mouse using hand gestures captured through a webcam. The system uses machine learning–based hand landmark detection to recognize gestures and perform mouse actions such as cursor movement and clicking.

The project integrates a Django web interface to start and stop the virtual mouse, while the ML engine runs as a background Python process to handle real-time gesture recognition and mouse control.
**
🎯 Objectives**

To control the system mouse using hand gestures

To reduce dependency on physical mouse devices

To demonstrate real-time computer vision and ML integration

To build a user-friendly control interface using Django

**🛠️ Technologies Used**
Programming Language

Python 3.x

Framework & Libraries

Django – Web interface and control panel

OpenCV – Webcam access and video processing

MediaPipe – ML-based hand landmark detection

PyAutoGUI – System mouse control

NumPy – Mathematical computations

**
⚙️ How the System Works**

The user opens the Django web application.

Clicking Start Virtual Mouse launches the ML engine.

OpenCV captures real-time video from the webcam.

MediaPipe detects hand landmarks using a pre-trained ML model.

Hand gestures are interpreted using finger positions.

PyAutoGUI converts recognized gestures into mouse movements and clicks.

Clicking Stop Virtual Mouse terminates the ML process.
