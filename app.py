from flask import Flask, request, jsonify
import numpy as np
import joblib

# Load trained model
model = joblib.load("cybersecurity_model.pkl")

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # Expecting all 78 features in a list
        if "features" not in data:
            return jsonify({"error": "Missing 'features' key in request JSON"}), 400

        features = np.array(data["features"]).reshape(1, -1)

        prediction = model.predict(features)
        return jsonify({"Threat_Detected": bool(prediction[0])})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
