from ultralytics import YOLO

model = YOLO("yolov11_custom.pt")

model.predict(source="2.jpg", show=True, save=True)