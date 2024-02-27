import json
import os
import pandas as pd

working_directory = os.path.dirname(os.path.abspath(__file__))
path_to_data = working_directory + '\\data.json'

with open(path_to_data, 'r') as json_file:
    data = json.load(json_file)


labels = data['labels']
pm25 = data['datasets'][0]['data']
no2 = data['datasets'][1]['data']

df = pd.DataFrame({
    "Date": data["labels"],
    "PM2.5 (μg/m³)": pm25,
    "NO2 (μg/m³)": no2 
})

excel_file_path = working_directory + '\\date_poluare.xlsx'
df.to_excel(excel_file_path, index=False)

prompt = input('''DONE, WANT TO OPEN FILE? 
               1-Yes 
               2-No
               ''')

if int(prompt) == 1:
    os.startfile(working_directory + '\\date_poluare.xlsx')
else:
    exit()