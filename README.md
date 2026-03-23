# Real-Time Object Detection & Counting System

## Overview
This project is a real-time computer vision system designed to detect, track, and count objects such as vehicles and people using video streams and webcam input. It leverages the YOLOv8 deep learning model for object detection and the SORT algorithm for multi-object tracking.

The system can be applied to smart surveillance, traffic analysis, and crowd monitoring use cases.

## Features
- Real-time object detection using YOLOv8
- Multi-object tracking with SORT algorithm
- Vehicle counting from traffic footage
- People counting from webcam and escalator feeds
- High-speed inference with accurate object ID tracking

## Technologies Used
- Python
- YOLOv8
- OpenCV
- SORT Algorithm
- Computer Vision

## System Architecture
1. Video/Webcam input
2. Frame preprocessing using OpenCV
3. Object detection using YOLOv8
4. Object tracking using SORT
5. Real-time counting and visualization

## Installation
```bash
pip install ultralytics opencv-python numpy
