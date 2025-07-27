# 📄 backend/models/plant_model.py

plant_schema = {
    "name": str,
    "photo_url": str,
    "location": {
        "lat": float,
        "lon": float
    },
    "uploaded_by": str,
    "health_status": str,
    "growth_timeline": list,
    "journal_entries": list,
    "timestamp": str
}
