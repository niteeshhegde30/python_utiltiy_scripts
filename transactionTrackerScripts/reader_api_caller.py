import requests
from datetime import datetime

# API endpoint
get_url = "http://localhost:8080/api/transactionService/readTransactions"

headers = {
    "Content-Type": "application/json",
}

date_filter = datetime.now().strftime("%Y-%m-%d")
print(date_filter)

filter = {
    # "amount": 5, 
    # "comment" : "",
    # "category" : "dummry_category",
    "subCategory" : "dummry_sub_category",
    # "startDate" : "2023-12-14",
    # "endDate" : "2025-12-14"
    # "startDate" : datetime.now().strftime("%Y-%m-%d"),
    # "format" : "json"
}

response = requests.get(get_url, params=filter )

if response.status_code == 200:
    print("Success:", response)  # If response is in JSON format
    # print("Success:", response.text) 
    for object in response.json():
        print(object)
else:
    print("Error:", response.status_code, response.text)