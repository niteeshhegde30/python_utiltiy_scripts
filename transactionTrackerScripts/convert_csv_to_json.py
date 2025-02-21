import math
import json
import pandas as pd
from datetime import datetime

input_csv_file_path =  r"input_csv_file_path"
output_json_file_path = r"output_json_file_path"

column_mapping = {
    "Date": "date",
    "Amount": "amount",
    "Category": "category",
    "Subcategory": "subCategory",
    "Note": "comment"
}

def convert_to_standard_date(date_str):
    formats = ["%d-%m-%Y", "%m/%d/%Y %H:%M:%S"] 

    for fmt in formats:
        try:
            parsed_date = datetime.strptime(date_str, fmt)
            return parsed_date.strftime("%Y-%m-%d")  
        except ValueError:
            continue

    return None

def modify_values(row):
    row["date"] = convert_to_standard_date(row["date"])
    return row

df = pd.read_csv(input_csv_file_path, usecols=column_mapping.keys()).rename(columns=column_mapping)

df = df.apply(modify_values, axis=1)

def clean_json_object(json_obj):
    return {k: v for k, v in json_obj.items() if v is not None and not (isinstance(v, float) and math.isnan(v))}


json_objects = []
for index, row in df.iterrows():
    json_obj = row
    json_obj = clean_json_object(json_obj)
    json_objects.append(json_obj)

print('total objects = ', len(json_objects))

with open(output_json_file_path, "w") as f:
    json.dump(json_objects, f, indent=4)

print(f"JSON file '{output_json_file_path}' saved successfully!")