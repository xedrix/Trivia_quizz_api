import requests

PARAMS = {
    "amount": 50,
    "category": 15,
    "type": "boolean"
}

response = requests.get(url="https://opentdb.com/api.php", params=PARAMS)
data = response.json()["results"]
question_data = [question for question in data]
