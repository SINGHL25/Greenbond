import streamlit as st
import folium
from streamlit_folium import st_folium
from app.services.firebase_service import fetch_all_plants

def render():
    st.title("🌍 Environmental Plantation Tracker")

    plant_data = fetch_all_plants()

    m = folium.Map(location=[-25.2744, 133.7751], zoom_start=4)

    for plant in plant_data:
        folium.Marker(
            location=[plant['lat'], plant['lon']],
            popup=f"{plant['name']} ({plant['health']})",
            tooltip="Click for details",
            icon=folium.Icon(color='green')
        ).add_to(m)

    st_data = st_folium(m, width=1000, height=500)

