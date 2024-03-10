# app.py
from flask import Flask, jsonify, request
import uuid

app = Flask(__name__)

todos = []

@app.route('/todos', methods=['GET'])
def get_todos():
    """Get all todo items."""
    return jsonify(todos)

# Define other endpoints for managing todo items (GET, POST, PUT, DELETE)

if __name__ == '__main__':
    app.run(debug=True)
