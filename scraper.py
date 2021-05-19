import requests, json, random, time
import pandas as pd


def get_seven_store(lat, long):
    iserror=False
    url = "https://www.7eleven.co.th/api/v1/Store/GetStoreByCurrentLocation"
    payload = {"latitude": lat, "longitude": long} 
    headers = {'Accept': 'application/json, text/plain, */*'}
    response = requests.post(url, headers=headers, data=payload)
    json_data = response.json()
    return json_data


tambon_lat_long_df = pd.read_excel('kh-muulphikad-lat-long-thiibngchiichuue-tambl-ameph-cchanghwad.xlsx')  
tambon_lat_long_df = tambon_lat_long_df[["TA_ID", "LAT", "LONG"]]
tambon_lat_long_df = tambon_lat_long_df.drop_duplicates(subset='TA_ID', keep="first")
tambon_lat_long_df = tambon_lat_long_df.sort_values(by=['TA_ID'])
tambon_lat_long_df = tambon_lat_long_df.reset_index()
print(tambon_lat_long_df.head())

for index, row in tambon_lat_long_df[156:].iterrows():
    print(index, row['TA_ID'], row['LAT'], row["LONG"])
    filename = f"raw-data/{index}_{int(row['TA_ID'])}.json"
    json_data = get_seven_store(row['LAT'], row['LONG'])
    with open(filename, 'w') as outfile: json.dump(json_data, outfile, ensure_ascii=False)
    sleep_time = random.randint(30, 60)
    time.sleep(sleep_time)

