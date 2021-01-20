import requests
import json
import pandas as pd

URL = "https://connection.eu-central-1.keboola.com/v2/storage/files"

with open("config.json","r") as f:
    config = json.load(f)


offset = 0
params = {"showExpired":"true","limit":"1","offset":"0"}
response = requests.get(url=URL,headers=config,params=params)

with open("data.json","w") as f:

    while response.text != "[]":
        offset += 100
        params['offset'] = str(offset)
        response = requests.get(url=URL,headers=config,params=params)

    params['offset'] = str(0)
    params['limit'] = str(offset)
    response = requests.get(url=URL,headers=config,params=params)
    f.write(response.text)


df = pd.read_json("data.json")
df.to_csv("response.csv", index = None)
