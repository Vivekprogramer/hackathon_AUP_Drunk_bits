# DJI Tello Drone Live Feed
import cv2
from djitellopy import Tello

tello = Tello()
tello.connect()
tello.streamon()

while True:
    frame = tello.get_frame_read().frame
    results = model.predict(frame)  # YOLO inference
    cv2.imshow("Live Detection", results.render())
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break