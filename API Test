#This code is used to test if Meraki API works


import requests

# Replace with your actual API key
API_KEY = "YOUR_API_KEY"
ORG_ID = "YOUR_ORG_ID"

url = f"https://api.meraki.com/api/v1/organizations/{ORG_ID}/networks"

headers = {
    "X-Cisco-Meraki-API-Key": API_KEY,
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    networks = response.json()
    print("Meraki API is working. Networks found:")
    for net in networks:
        print(f"- {net['name']} (ID: {net['id']})")
else:
    print("API request failed with status {response.status_code}: {response.text}")
