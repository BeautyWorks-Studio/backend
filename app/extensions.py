from mongoengine import connect
import os
from dotenv import load_dotenv

load_dotenv()

def init_db(app=None):
    """Initialize MongoDB connection."""
    mongo_uri = os.getenv("MONGODB_URI")
    if not mongo_uri:
        raise ValueError("MONGODB_URI not set in .env file")
    connect(host=mongo_uri)

