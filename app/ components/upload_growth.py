import streamlit as st
from app.services.firebase_service import upload_growth_photo
from datetime import datetime

def render(user_id: str):
    st.title("📸 Upload Plant Growth")

    uploaded_file = st.file_uploader("Take a new picture or upload recent plant photo", type=["jpg", "jpeg", "png"])
    caption = st.text_input("Add a caption about this growth stage")

    if st.button("Upload") and uploaded_file:
        upload_growth_photo(user_id, uploaded_file, caption, str(datetime.now()))
        st.success("✅ Growth photo uploaded successfully!")

