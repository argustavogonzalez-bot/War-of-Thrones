from flask import Flask
from flask_socketio import SocketIO

# Create the Flask application
app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return 'Welcome to the War of Thrones Game!'

if __name__ == '__main__':
    socketio.run(app, debug=True)