import requests

response = requests.get("http://192.168.100.28:8888/my_func")
print(response.json())