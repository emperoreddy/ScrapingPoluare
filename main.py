import json
import os
import pandas as pd

# Determine the working directory
working_directory = os.path.dirname(os.path.abspath(__file__))
path_to_data = os.path.join(working_directory, 'data.json')

# Load the JSON data
with open(path_to_data, 'r') as json_file:
    data = json.load(json_file)

# Extract data
labels = data['labels']
pm25 = data['datasets'][0]['data']
no2 = data['datasets'][1]['data']

# Create DataFrame
df = pd.DataFrame({
    "Date": labels,
    "PM2.5 (μg/m³)": pm25,
    "NO2 (μg/m³)": no2 
})

# Determine the directory for the Excel files
output_directory = os.path.join(working_directory, 'DATE POLUARE')

# Ensure the directory exists
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Find the next available filename
existing_files = [f for f in os.listdir(output_directory) if f.endswith('.xlsx')]
existing_numbers = [int(os.path.splitext(f)[0]) for f in existing_files if f.split('.')[0].isdigit()]
next_number = max(existing_numbers, default=0) + 1
excel_file_path = os.path.join(output_directory, f'{next_number}.xlsx')

# Save the DataFrame to the next Excel file
df.to_excel(excel_file_path, index=False)

# prompt = input('''DONE, WANT TO OPEN FILE? 
#                1-Yes 
#                2-No
#                ''')

# if int(prompt) == 1:
#     os.startfile(working_directory + '\\date_poluare.xlsx')
# else:
#     exit()