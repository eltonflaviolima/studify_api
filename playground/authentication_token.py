import requests

url = 'http://127.0.0.1:8000/api/'
headers = {'Authorization': 'Token <TOKEN GERADO>'}
r = requests.get(url, headers=headers)
print(r)