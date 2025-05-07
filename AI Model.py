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

model = DecisionTreeClassifier()
model.fit(X, y)

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

if __name__ == "__main__":
    prediction = predict_channel(test_input)
    print("Recommended Channel:", prediction)

    API_KEY = "YOUR_API_KEY"
    AP_SERIAL = "YOUR_AP_SERIAL"

    push_channel_to_meraki(API_KEY, AP_SERIAL, prediction)



