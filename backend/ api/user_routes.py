# 📄 backend/api/user_routes.py

from fastapi import APIRouter
from models import user_model

router = APIRouter()

@router.post("/create_user")
def create_user(data: dict):
    # Add to Firebase
    return {"message": "User created", "data": data}

@router.get("/user/{uid}")
def get_user(uid: str):
    return {"user": {"uid": uid}}  # Replace with Firebase fetch
