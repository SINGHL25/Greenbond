import streamlit as st
from app.services.firebase_service import fetch_community_posts

def render():
    st.title("🌿 Community Feed")
    
    posts = fetch_community_posts()
    
    for post in posts:
        with st.expander(f"{post['user']} - {post['title']}"):
            st.markdown(f"📝 {post['content']}")
            st.caption(f"📅 {post['timestamp']}")

