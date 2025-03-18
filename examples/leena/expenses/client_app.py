import requests

print(requests.get("http://localhost:8888/my_func").json())