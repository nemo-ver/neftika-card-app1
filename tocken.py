import requests
import json

url = 'https://log.neftika-card.ru:48000/token'
payload = {
    'Username': 'API1',
    'Password': 'U71(K}',
    'Grant_type': 'password'
}
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.post(url, data=payload, headers=headers, verify=False)

if response.status_code == 200:
    tocken=json.loads(response.text)
else:
    print(f"Request failed with status code: {response.status_code}")


