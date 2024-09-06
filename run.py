from flask import Flask, jsonify
from app.routes import app  # Import the entire app instance
from flask_cors import CORS
from flask_socketio import SocketIO

CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return 'Socket.IO server running'


if __name__ == '__main__':
     socketio.run(app, debug=True)
