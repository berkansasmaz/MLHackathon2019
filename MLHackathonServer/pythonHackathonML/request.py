import requests
import json

url = 'http://localhost:5000/predict'
headers = {'content-type': 'application/json'}
payload = [
    {'mesaj':'güzel üründü tebrikler gönderim için'}
]
response = requests.post(url, data=json.dumps(payload), headers=headers)

print(response.text)
