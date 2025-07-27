import firebase_admin
from firebase_admin import credentials, firestore, storage
import uuid

# Initialize Firebase only once
if not firebase_admin._apps:
    cred = credentials.Certificate("secrets/firebase_config.json")
    firebase_admin.initialize_app(cred, {
        'storageBucket': 'your-firebase-project-id.appspot.com'
    })

db = firestore.client()
bucket = storage.bucket()

# ---------------------- Plant Data ----------------------
def fetch_plant_by_id(plant_id):
    doc = db.collection("plants").document(plant_id).get()
    return doc.to_dict() if doc.exists else {}

def fetch_all_plants():
    docs = db.collection("plants").stream()
    return [doc.to_dict() for doc in docs]

# ---------------------- Community Feed ----------------------
def fetch_community_posts():
    docs = db.collection("community_posts").order_by("timestamp", direction=firestore.Query.DESCENDING).stream()
    return [doc.to_dict() for doc in docs]

def post_to_community(post):
    db.collection("community_posts").add(post)

# ---------------------- Emotion Journal ----------------------
def save_emotion_entry(entry):
    db.collection("emotions").add(entry)

# ---------------------- Growth Tracker ----------------------
def upload_growth_photo(user_id, file, caption, timestamp):
    blob_name = f"{user_id}/{uuid.uuid4()}.jpg"
    blob = bucket.blob(blob_name)
    blob.upload_from_file(file, content_type="image/jpeg")
    blob.make_public()

    db.collection("growth_photos").add({
        "user_id": user_id,
        "image_url": blob.public_url,
        "caption": caption,
        "timestamp": timestamp
    })

