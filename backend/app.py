from flask import Flask
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.routes import setup_routes

app = Flask(__name__)

# Register routes before running the app
setup_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
