import os
import requests
import json

def get_list_of_tools(url: str = "http://127.0.0.1:5000/get-list"):
    return json.loads(requests.get(url).content.decode("utf-8"))

print(get_list_of_tools())