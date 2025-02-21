import json
import requests

json_objects_file_path = r"json_objects_file_path"

post_url = "http://localhost:8080/api/transactionService/addTransactions"

headers = {
    "Content-Type": "application/json",
}

data = [
    {
        "amount": 270.5, 
        "date": "2024-12-11", 
        "comment": "abc",
        "category": "dummry_category",
        "subCategory": "dummry_sub_category"
    }
]

with open(json_objects_file_path, "r") as f:
    json_objects = json.load(f)

response = requests.post(post_url, json=json_objects, headers=headers)

if response.status_code == 200:
    print("Success:", response)  
    print("Success:", response.text) 
else:
    print("Error:", response.status_code, response.text)