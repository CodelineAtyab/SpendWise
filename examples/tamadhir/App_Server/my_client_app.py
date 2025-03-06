import requests

response = requests.get("http://192.168.100.106:8888/view_amount")
print(response.json())