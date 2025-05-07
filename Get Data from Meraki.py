#code to get data from Meraki dashborad 
#This is including the following: wireless status, channel utilization, number of client, signal Quality, Health Metrics 
import os
import requests

API_KEY = "YOUR_API_KEY"
NETWORK_ID = "YOUR_NETWORK_ID"
HEADERS = {
    "X-Cisco-Meraki-API-Key": API_KEY,
    "Content-Type": "application/json"
}

def get_wireless_status():
    url = f"https://api.meraki.com/api/v1/networks/{NETWORK_ID}/wireless/status"
    return requests.get(url, headers=HEADERS).json()

def get_channel_utilization():
    url = f"https://api.meraki.com/api/v1/networks/{NETWORK_ID}/wireless/channelUtilization"
    return requests.get(url, headers=HEADERS).json()

def get_clients():
    url = f"https://api.meraki.com/api/v1/networks/{NETWORK_ID}/clients"
    return requests.get(url, headers=HEADERS).json()

def get_signal_quality():
    url = f"https://api.meraki.com/api/v1/networks/{NETWORK_ID}/wireless/signalQuality"
    return requests.get(url, headers=HEADERS).json()


def get_wireless_health_metrics():
    url = f"https://api.meraki.com/api/v1/networks/{NETWORK_ID}/wireless/health/issues"
    return requests.get(url, headers=HEADERS).json()

def fetch_all_metrics():
    return {
        "status": get_wireless_status(),
        "channel_utilization": get_channel_utilization(),
        "client_count": len(get_clients()),
        "signal_quality": get_signal_quality(),
        "rf_beacons": get_rf_profile_beacons(),
        "health_issues": get_wireless_health_metrics()
    }

if __name__ == "__main__":
    metrics = fetch_all_metrics()
    print("Aggregated Wireless Metrics (for AI input):")
    print(metrics)


with open(script_path, "w") as f:
    f.write(health_script)

