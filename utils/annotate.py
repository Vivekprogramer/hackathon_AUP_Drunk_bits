# Uses Roboflow API to label images (alternative: CVAT)
import roboflow

rf = roboflow.Roboflow(api_key="YOUR_API_KEY")
project = rf.workspace().project("plastic-waste")
dataset = project.version(1).download("yolov8")