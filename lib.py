import requests
import json

URL = "https://wapt.pythonanywhere.com/"

def get_list_of_tools(url: str = "http://127.0.0.1:5000/get-list?query=", query: str = ""):
    if query == " " or query == None:
        query = ""
    else:
        query = "get-list?query=" + query
    url = URL + query
    return json.loads(requests.post(url).content.decode("utf-8"))

def install_package(pkg):
    pass

def deploy(folder):
    # zazipovat slozku do slozky v /zip adresari aplikace, pak odeslat na web
    if False:
        url = URL + "add-"
        requests.put(url)
    pass