import requests, json, random, time
import pandas as pd


def get_seven_store(lat:float, long:float):
    """ Reuest api with post method to 7elven     
        Arguments: lat, long
        Returns: json_data
    """
    url = "https://www.7eleven.co.th/api/v1/Store/GetStoreByCurrentLocation"
    payload = {"latitude": lat, "longitude": long} 
    headers = {'Accept': 'application/json, text/plain, */*'}
    response = requests.post(url, headers=headers, data=payload)
    json_data = response.json()
    return json_data

""" Read tambon df and use TA_ID to scrape location based on Thai Tambon"""
selected_province_list = ["กรุงเทพมหานคร", "จ. สมุทรปราการ", "จ. นนทบุรี", "จ. ปทุมธานี", "จ. นครปฐม", "จ. สมุทรสงคราม"]
tambon_lat_long_df = pd.read_excel('kh-muulphikad-lat-long-thiibngchiichuue-tambl-ameph-cchanghwad.xlsx')  
tambon_lat_long_df = tambon_lat_long_df[tambon_lat_long_df.CHANGWAT_T.isin(selected_province_list)]
tambon_lat_long_df = tambon_lat_long_df[["TA_ID", "LAT", "LONG"]]
tambon_lat_long_df = tambon_lat_long_df.drop_duplicates(subset='TA_ID', keep="first")
tambon_lat_long_df = tambon_lat_long_df.sort_values(by=['TA_ID'])
tambon_lat_long_df = tambon_lat_long_df.reset_index()
print(tambon_lat_long_df.head())

RESULT_DIRECTORY = "raw-data"
print("Total api calls:", len(tambon_lat_long_df))
for index, row in tambon_lat_long_df.iterrows():
    print(index, row['TA_ID'], row['LAT'], row["LONG"])
    filename = f"{RESULT_DIRECTORY}/{index}_{int(row['TA_ID'])}.json"
    json_data = get_seven_store(row['LAT'], row['LONG'])
    with open(filename, 'w') as outfile: json.dump(json_data, outfile, ensure_ascii=False)
    sleep_time = random.randint(30, 90)
    time.sleep(sleep_time)

