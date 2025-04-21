import streamlit as st
from PIL import Image
import requests

st.title("♻️ PlastEye: AI Waste Detector")
uploaded_file = st.file_uploader("Upload Drone Image")

if uploaded_file:
    col1, col2 = st.columns(2)
    with col1:
        st.image(uploaded_file, caption="Original")
    
    # Call FastAPI backend
    response = requests.post(
        "http://localhost:8000/predict",
        files={"file": uploaded_file.getvalue()}
    )
    detections = response.json()["detections"]
    
    with col2:
        st.image("temp_result.jpg", caption="Detected Waste")  # Replace with actual rendering
        st.download_button("Download Heatmap", "heatmap.html")