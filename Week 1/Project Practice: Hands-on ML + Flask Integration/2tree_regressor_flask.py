from flask import Flask, request, jsonify
import numpy as np
import pickle
import pandas as pd


# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model = pickle.load(open("tree.pkl", "rb"))

@app.route('/')
def home():
    return "ML Model Flask API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON input
        data = request.get_json()
        
        # Convert JSON input into a NumPy array
        input_features = np.array(data["features"]).reshape(1, -1)

        # Make prediction
        prediction = model.predict(input_features)[0]

        # Return the result as JSON
        return jsonify({"predicted_value": round(prediction, 2)})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(port=8080,debug=True)
