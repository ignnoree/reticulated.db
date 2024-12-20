
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'retyculated_databases')
    RETICULATED_FOLDER=os.path.join(os.getcwd(), 'retyculated_databases')
    SECRET_KEY = 'your_secret_key'
    os.makedirs(RETICULATED_FOLDER, exist_ok=True) 
    
