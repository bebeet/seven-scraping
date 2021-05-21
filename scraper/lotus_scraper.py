import requests, json
url = "https://www.tescolotus.com/location/json_list?t=1621604570256"
params = { "category": 999 }
headers = {'Accept': 'application/json, text/plain, */*'}
response = requests.get(url, headers=headers, params=params)
json_data = response.json()
with open("lotus_data.json", 'w') as outfile: json.dump(json_data, outfile, ensure_ascii=False)