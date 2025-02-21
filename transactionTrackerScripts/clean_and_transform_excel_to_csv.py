import pandas as pd
import re

print("starting the execution")
file_path = r"path of the excel file to be cleaned" 
new_file_path =  r"path of the cleaned csv file"
columns_to_be_cleaned = ["Category", "Subcategory"]

def clean_column(value):
    if isinstance(value, str):
        return re.sub(r'^[^a-zA-Z]+', '', value)
    return value

df = pd.read_csv(file_path, encoding="utf-8", dtype=str)  

for column in columns_to_be_cleaned:
    df[column] = df[column].apply(clean_column) 

df.to_csv(new_file_path, index=False, encoding="utf-8")

print("cleaned and saved the excel file into csv")