import streamlit as st
from app.map_view import show_map_view
from app.plant_profile import show_plant_profile
from app.upload_growth import show_growth_upload
from app.community_feed import show_community_feed
from app.emotion_journal import show_emotion_journal

st.set_page_config(page_title="GreenConnect 🌿", layout="wide")

PAGES = {
    "🗺️ Map View": show_map_view,
    "🪴 Plant Profile": show_plant_profile,
    "📤 Upload Growth Photo": show_growth_upload,
    "🌱 Community Feed": show_community_feed,
    "🧠 Emotion Journal": show_emotion_journal,
}

st.sidebar.title("GreenConnect Menu")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
PAGES[selection]()

