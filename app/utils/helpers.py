 📄 app/utils/helpers.py

import datetime

def format_timestamp():
    return datetime.datetime.utcnow().isoformat()

def truncate(text, limit=80):
    return text[:limit] + ("..." if len(text) > limit else "")
