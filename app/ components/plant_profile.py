import streamlit as st
from app.services.firebase_service import fetch_plant_by_id

def render(plant_id: str):
    plant = fetch_plant_by_id(plant_id)
    
    st.header(f"🌱 {plant['name']} Profile")
    st.image(plant["image_url"], caption=plant["name"], use_column_width=True)

    st.subheader("📊 Plant Details")
    st.markdown(f"**Species:** {plant['species']}")
    st.markdown(f"**Health Status:** {plant['health']}")
    st.markdown(f"**Location:** {plant['lat']}, {plant['lon']}")
    st.markdown(f"**Planted On:** {plant['planted_on']}")

    st.subheader("📖 Story")
    st.info(plant["description"])

