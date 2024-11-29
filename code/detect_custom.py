from ultralytics import YOLO

model = YOLO("yolov11_custom2.pt")

model.predict(source="./images/7.jpg", show=True, save=True,conf=0.4)