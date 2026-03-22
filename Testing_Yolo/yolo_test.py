import torch
import functools

torch.load = functools.partial(torch.load, weights_only=False)

from ultralytics import YOLO
import cv2

model = YOLO('../Yolo-Weights/yolov8l.pt')
results = model("Images/3.jpg", show = True)
cv2.waitKey(0)

