import requests

endpoint = 'https://httpbin.org/status/200'
endpoint = 'https://httpbin.org/anything'
endpoint = 'http://localhost:8000/survey-api-home'
endpoint = 'http://localhost:8000/survey-api-home-2'
endpoint = 'http://localhost:8000/survey-api-home-post'

response = requests.post(endpoint,params={"user": "farid"}, json={"name1": "new-company"})
print(response.json())
print(response.status_code)