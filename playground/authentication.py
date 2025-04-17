import requests
import json

url = 'http://127.0.0.1:8000/api/auth/login/'
body = {
    'username':'eltonflavio',
    'password':'1234'
    }
r = requests.post(url, data=body)
print(r.json())