import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///beauty.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
