import requests
import json
import os
import zipfile

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

def zip_folder(folder_path, output_zip):
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, folder_path)
                zipf.write(file_path, arcname)

def deploy(folder, name):
    # zazipovat slozku do slozky v /zip adresari aplikace, pak odeslat na web
    if os.path.exists(folder):
        zip_folder(folder, name)
    if False:
        url = URL + "add-"
        requests.put(url)
    pass