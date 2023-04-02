import os
from dotenv import load_dotenv

load_dotenv()

class Config():
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '')
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER', './uploads')
    SECRET_KEY = os.environ.get('SECRET_KEY')

