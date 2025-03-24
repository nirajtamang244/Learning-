import requests

url = "http://127.0.0.1:5000/add"  # Change the endpoint to match the API
data = {"a": 5, "b": 10}  # JSON data for POST request

response = requests.post(url, json=data)  # Sending JSON data
print(response.json())  # Prints the predicted output
