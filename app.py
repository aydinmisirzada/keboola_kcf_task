import requests
import json
import pandas as pd

URL = "https://connection.north-europe.azure.keboola.com/v2/storage/files"

with open("config.json","r") as f:
    config = json.load(f)

params = {"showExpired":"true"}
response = requests.get(url=URL,headers=config,params=params)

with open("data.json","w") as f:
    f.write(response.text)

df = pd.read_json("data.json")
df.to_csv("response.csv", index = None)
