import torch
import functools

# THE SAFETY PATCH: Tells PyTorch to trust the YOLO model file
torch.load = functools.partial(torch.load, weights_only=False)

# Now your imports can happen
from ultralytics import YOLO
import cv2

