import requests
import json
import pytest
import jsonpath

# Create Trello Workspace via Pytest API

def test_post():

    url = "https://api.trello.com/1/boards/"

    query = {
    "key": "######################", # Get your own key on Trello
    "token": "####################", # Get your own token on Trello
    "name": "Test via python" # Workspace Name
}

    response = requests.post(url,params=query)
    code = response.status_code
    assert code == 200

    json_response = json.loads(response.text)
    name = jsonpath.jsonpath(json_response,'name')

    assert name == ["Test via pytest"]