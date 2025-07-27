import streamlit as st
from datetime import datetime
from app.services.firebase_service import save_emotion_entry

def render(user_id: str):
    st.title("💚 Emotion Journal with Your Plant")

    mood = st.radio("How do you feel around your plant today?", ["😊 Happy", "😌 Calm", "😢 Sad", "😠 Frustrated"])
    notes = st.text_area("Write a note about your experience or emotion today")

    if st.button("Save Entry"):
        entry = {
            "user_id": user_id,
            "mood": mood,
            "notes": notes,
            "timestamp": str(datetime.now())
        }
        save_emotion_entry(entry)
        st.success("🧠 Emotion saved! Your plant thanks you for connecting 💖")

