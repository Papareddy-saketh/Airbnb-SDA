from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load your models
models = {
    'model1': pickle.load(open('gradient_boosting_model.pkl', 'rb')),
    'model2': pickle.load(open('label_encoders.pkl', 'rb'))  
}

@app.route('/')
def home():
    return render_template('app.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    model_name = data.get('model')
    user_id = data.get('user_id')
    
    if not model_name or not user_id:
        return jsonify({'error': 'Invalid input'}), 400

    if model_name not in models:
        return jsonify({'error': 'Model not found'}), 400

    model = models[model_name]

    prediction = f"Prediction for user {user_id} using {model_name}"
    return jsonify({'result': prediction})

if __name__ == '__main__':
    app.run(debug=True)
