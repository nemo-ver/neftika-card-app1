import requests
import json
import config

def getdata(StartDate,FinishDate):
    url = config.TOKEN_URL
    payload = {
        'Username': config.API_USERNAME,
        'Password': config.API_PASSWORD,
        'Grant_type': 'password'
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.post(url, data=payload, headers=headers, verify=False)

    if response.status_code == 200:
        token=json.loads(response.text)
    else:
        print(f"Request failed with status code: {response.status_code}")


    url = config.REPORT_URL
    params = {
        'dateStart': StartDate,
        'dateFinish': FinishDate
    }
    headers = {
        'Authorization': token["token_type"]+' '+ token["access_token"]
    }

    response = requests.get(url, params=params, headers=headers, verify=False)

    if response.status_code == 200:
        filepath="./download/"+StartDate+"-"+FinishDate+".json"
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(response.text)
        return filepath
    else:
        print(f"Request failed with status code: {response.status_code}")