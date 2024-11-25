import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    print("Error: API_KEY is not working")
    exit()

platform = "steam"
platformUserIdentifier = "76561198333152420"  

# Construct the API endpoint
url = f"https://public-api.tracker.gg/v2/csgo/standard/profile/{platform}/{platformUserIdentifier}"


headers = {
    "TRN-Api-Key": API_KEY
}

#GET request
response = requests.get(url, headers=headers)

# Check request is successful
if response.status_code == 200:
    data = response.json()
    print("API Response:", data)
else:
    print(f"Error: {response.status_code}")
    print("Response text:", response.text)
