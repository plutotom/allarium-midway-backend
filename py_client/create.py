import requests

endpoint = 'http://localhost:8000/api/tenant/'

response = requests.post(endpoint,params={"user": "farid"}, json={"name": "new-company1234"})
print(response.json())
print(response.status_code)