# EECS261-Final-Project
# Meraki AI-Based Channel Optimizer

This program leverages machine learning to optimize Wi-Fi performance by dynamically adjusting channel assignments on Cisco Meraki access points. 
It integrates with the Meraki Dashboard API to collect real-time telemetry data—such as channel utilization, noise levels, 
and connected client counts—and uses this data to train a simple decision tree model that can recommend the best Wi-Fi channel for a given set of RF conditions. 
The model's output is then pushed back to the APs via the Meraki API, automating what would otherwise be a manual and reactive network tuning process.

The system is modularized for clarity and maintainability. It includes a Flask-based REST API to expose the AI prediction engine,
Python scripts for interacting with Meraki's API to pull telemetry or push new settings, and an isolated ML module for training and inference. 
It is designed to be extendable—future iterations could include more complex models (e.g., using TensorFlow), historical training data stored in a database, 
or full dashboard integration for enterprise environments. 
