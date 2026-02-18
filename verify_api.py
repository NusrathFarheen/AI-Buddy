import requests
import json

url = "http://localhost:8000/api/goals"
payload = {
    "title": "Launch a successful Podcast",
    "description": "I want to start a tech podcast. I have no equipment.",
    "deadline": "2026-03-01"
}
headers = {"Content-Type": "application/json"}

try:
    response = requests.post(url, json=payload, headers=headers)
    print(f"Status Code: {response.status_code}")
    print("Response JSON:")
    print(json.dumps(response.json(), indent=2))
except Exception as e:
    print(f"Error: {e}")
