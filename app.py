import requests
import json


URL = "https://connection.eu-central-1.keboola.com/v2/storage/files"

with open("config.json","r") as f:
    config = json.load(f)

offset = 0
limit = 100
params = {"showExpired":"true","limit":"100","offset":"0"}

response = requests.get(url=URL,headers=config,params=params)
with open("response.csv","a") as f:
    json_list = json.loads(response.text)
    f.write(','.join(json_list[0].keys())+'\n')
    for file in json_list:
        f.write(','.join(str(x) for x in file.values())+'\n')

    while response.text != "[]":
        offset += 100
        params['offset'] = str(offset)
        response = requests.get(url=URL,headers=config,params=params)
        if response.text != "[]":
            json_list = json.loads(response.text)
            for file in json_list:
                f.write(','.join(str(x) for x in file.values())+'\n')
