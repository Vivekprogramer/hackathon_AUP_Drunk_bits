from fastapi import FastAPI, UploadFile
from PIL import Image
import io
from ultralytics import YOLO

app = FastAPI()
model = YOLO("models/yolov8_plastic.pt")

@app.post("/predict")
async def predict(file: UploadFile):
    image = Image.open(io.BytesIO(await file.read()))
    results = model.predict(image)
    return {"detections": results[0].boxes.xyxy.tolist()}