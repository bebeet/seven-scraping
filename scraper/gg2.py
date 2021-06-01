import requests, json, random, time
import pandas as pd

api_key="AIzaSyDQxCKOSaHSfhKv4t6cgzDQk4dW9DFDHqA" 


def gg_place_api(lat, long):
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {"key": api_key, "query": "เซเว่น", "language":"th",
            "location":f"{lat},{long}","radius":10000,
            "fields":"formatted_address,name,rating,opening_hours,geometry"}
    response = requests.get(url, params=params)
    json_data = response.json()
    return json_data




""" Read tambon df and use TA_ID to scrape location based on Thai Tambon"""
selected_province_list = ["กรุงเทพมหานคร"]
tambon_lat_long_df = pd.read_excel("kh-muulphikad-lat-long-thiibngchiichuue-tambl-ameph-cchanghwad.xlsx")  
tambon_lat_long_df = tambon_lat_long_df[tambon_lat_long_df.CHANGWAT_T.isin(selected_province_list)]
tambon_lat_long_df = tambon_lat_long_df[["TA_ID", "TAMBON_T", "LAT", "LONG"]]
tambon_lat_long_df = tambon_lat_long_df.drop_duplicates(subset="TA_ID", keep="first")
tambon_lat_long_df = tambon_lat_long_df.sort_values(by=["TA_ID"])
tambon_lat_long_df = tambon_lat_long_df.reset_index()
print(tambon_lat_long_df.head())

RESULT_DIRECTORY = "raw-data"
print("Total api calls:", len(tambon_lat_long_df))
for index, row in tambon_lat_long_df.iterrows():
    print(index, row["TA_ID"], row["TAMBON_T"], row["LAT"], row["LONG"])
    json_data = gg_place_api(row["LAT"], row["LONG"])
    filename = f"{RESULT_DIRECTORY}/gg/{index}_{int(row['TA_ID'])}.json"
    with open(filename, "w") as outfile: json.dump(json_data, outfile, ensure_ascii=False)
    sleep_time = random.randint(1,10)
    time.sleep(sleep_time)