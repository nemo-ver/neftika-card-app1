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


url = 'https://log.neftika-card.ru:48000/api/TransactionReport'
params = {
    'dateStart': '2023-02-01',
    'dateFinish': '2023-03-01'
}
headers = {
    'Authorization': tocken["token_type"]+' '+ tocken["access_token"]
}

response = requests.get(url, params=params, headers=headers, verify=False)

if response.status_code == 200:
    with open("./output.txt", "w", encoding="utf-8") as file:
        file.write(response.text)
else:
    print(f"Request failed with status code: {response.status_code}")