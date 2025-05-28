import requests

url = "http://127.0.0.1:5000/predict"

# Dummy list of 78 values (you can replace this with actual scaled data if needed)
dummy_features = [0.0] * 78

data = {
    "features": dummy_features
}

response = requests.post(url, json=data)

try:
    print("Response:", response.json())
except Exception as e:
    print("Error parsing JSON:", e)
    print("Raw response:", response.text)
