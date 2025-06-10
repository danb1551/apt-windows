import requests
import json

def get_list_of_tools(url: str = "http://127.0.0.1:5000/get-list?query=", query: str = ""):
    if query == " " or query == None:
        query == ""
    url = url + query
    return json.loads(requests.post(url).content.decode("utf-8"))

def install_package(pkg):
    pass