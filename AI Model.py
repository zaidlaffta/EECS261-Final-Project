# This program is a machine learning-based recommend the optimal Wi-Fi channel

import json
import os
import joblib
import requests
from sklearn.tree import DecisionTreeClassifier

# Load training data
data_path = os.path.join(os.path.dirname(__file__), 'training_data.json')
with open(data_path, 'r') as file:
    data = json.load(file)

X = data['features']
y = data['labels']

# Train the model
model = DecisionTreeClassifier()
model.fit(X, y)

# Save the model
model_file = os.path.join(os.path.dirname(__file__), 'channel_predictor.joblib')
joblib.dump(model, model_file)

def predict_channel(input_features):
    return model.predict([input_features])[0]

def push_channel_to_meraki(api_key, ap_serial, channel):
    url = f"https://api.meraki.com/api/v1/devices/{ap_serial}/wireless/radioSettings"
    headers = {
        "X-Cisco-Meraki-API-Key": api_key,
        "Content-Type": "application/json"
    }
    payload = {
        "channel": int(channel),
        "power": 14
    }
    response = requests.put(url, headers=headers, json=payload)
    print("Meraki API response:", response.status_code, response.text)

# Example test and push
if __name__ == "__main__":
    test_input = [70, 22, 20, 250, 1, 1]
    prediction = predict_channel(test_input)
    print("Recommended Channel:", prediction)

    # Replace with actual values
    API_KEY = "YOUR_API_KEY"
    AP_SERIAL = "YOUR_AP_SERIAL"

    push_channel_to_meraki(API_KEY, AP_SERIAL, prediction)
"""

# Save updated script
updated_model_path = "/mnt/data/Meraki-AI-Channel-Optimizer/ml_model/train_and_push.py"
with open(updated_model_path, "w") as f:
    f.write(full_script_with_push)

updated_model_path

