from flask import Flask
from flask_cors import CORS

# Initializing
def create_app():
  app = Flask(__name__)
  CORS(app) # Enable CORS for React frontend
