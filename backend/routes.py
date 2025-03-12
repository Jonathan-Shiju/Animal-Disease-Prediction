from app import app
from flask import request, jsonify
from animal_disease_prediction.pipelines.prediction_pipeline import predict

def setup_routes(app):
    @app.route('/')
    def index():
        return "<h1>Connected to text model backend</h1>"

@app.route('/api/status')
def status():
    return {"message": "API is running", "status": "success"}

@app.route('/predict')
def predict():
    data = request.get_json()
    result = predict(data)
    return jsonify(result), 200
