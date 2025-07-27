# 📄 backend/api/plant_routes.py

from fastapi import APIRouter
from models import plant_model

router = APIRouter()

@router.post("/add_plant")
def add_plant(data: dict):
    # Save to DB
    return {"message": "Plant added", "data": data}

@router.get("/plants")
def get_all():
    return {"plants": []}  # Replace with Firebase fetch
