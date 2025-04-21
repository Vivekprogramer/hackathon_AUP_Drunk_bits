# YOLOv8 Training (Ultralytics)
from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # Load pretrained
results = model.train(
    data="data/annotated/data.yaml",
    epochs=50,
    imgsz=640,
    batch=8
)
model.export(format="onnx")  # Optional: Export for edge deployment