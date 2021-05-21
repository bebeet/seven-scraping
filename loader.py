""" Load all to GCS """
import glob, json 



RESULT_DIRECTORY = "raw-data"
data_files  = glob.glob(f"{RESULT_DIRECTORY}/*.json")

# Aggregrate json file 
data_all = []
for file in data_files:
    with open (file, "r") as f: data = json.loads(f.read())
    data_all += data


with open('seven_data.json', 'w') as outfile: json.dump(data_all, outfile, ensure_ascii=False) 


