import requests

# API endpoint
post_url = "http://localhost:8080/api/transactionService/addTransactions"
get_url = "http://localhost:8080/api/transactionService/"



headers = {
    "Content-Type": "application/json",
}

# Data to be sent in JSON format
data = [
    {"amount": 260.5, "date": "2024-12-11"}
]

# Making the POST request
response = requests.post(post_url, json=data, headers=headers)
# response = requests.get(get_url)

# Checking response status
if response.status_code == 200:
    print("Success:", response)  # If response is in JSON format
    print("Success:", response.text)  # If response is in JSON format
else:
    print("Error:", response.status_code, response.text)