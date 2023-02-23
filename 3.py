import requests
import json

# Create Trello Workspace via Python API

url = "https://api.trello.com/1/boards/"

query = {
    "key": "######################", # Get your own key on Trello
    "token": "####################", # Get your own token on Trello
    "name": "Test via python" # Workspace Name
}

response = requests.post(url,params=query)

# cetak response code
print(response.status_code)

# cetak json file
json_response = json.loads(response.text)
print(json_response)