from flask import Blueprint, jsonify

main_routes = Blueprint('main', __name__)

@main_routes.rout('/api/hello', methods=['GET'])
def hello():
  return jsonify({"message": "Hello from Flask!"})
