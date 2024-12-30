from flask import Flask
from flask_cors import CORS

# Initializing
def create_app():
  app = Flask(__name__)
  CORS(app) # Enable CORS for React frontend

  from .routes import main_routes
  app.register_blueprint(main_routes)

  return app
