# Uses DBSCAN clustering + Folium
import folium
from sklearn.cluster import DBSCAN
import numpy as np

def generate_heatmap(detections, output_path="heatmap.html"):
    coords = np.array([[d['lon'], d['lat']] for d in detections])
    clustering = DBSCAN(eps=0.01, min_samples=3).fit(coords)
    
    m = folium.Map(location=[coords[0][1], coords[0][0]], zoom_start=15)
    folium.HeatMap(coords).add_to(m)
    m.save(output_path)