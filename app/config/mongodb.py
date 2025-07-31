from mongoengine import connect
import os

def connect_db():
    connect(host=os.getenv("MONGODB_URI"))
