import requests
import json
import os
import zipfile

URL = "https://wapt.pythonanywhere.com/"
LOCAL = True

def get_list_of_tools(url: str = "http://127.0.0.1:5000/get-list?query=", query: str = ""):
    if LOCAL:
        url = "http://127.0.0.1:5000/get-list?query="
    else:
        url = URL + "get-list?query="
    if query == " " or query == None:
        query = ""
    else:
        query = "get-list?query=" + query
    url = URL + query
    return json.loads(requests.post(url).content.decode("utf-8"))

def install_package(pkg: str):
    if pkg.endswith(".zip"):
        output_path = os.path.join("C:\\wapt\\", pkg)
    else:
        output_path = os.path.join("C:\\wapt\\", pkg + ".zip")
    if LOCAL:
        url = f"http://127.0.0.1:5000/tools/{pkg}"
    else:
        url = URL + f"tools/{pkg}"
    response = requests.get(url)
    if response.status_code == 200:
        with open(output_path, 'wb') as f:
            f.write(response.content)
    zip_file = output_path
    out_fol = os.path.join("C:\\wapt\\", pkg)
    unzip_folder(zip_file, out_fol)

def zip_folder(folder_path, output_zip):
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, folder_path)
                zipf.write(file_path, arcname)

def unzip_folder(zip_path, output_folder):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(output_folder)

def deploy(folder: str, name: str, author: str):
    # zazipovat slozku do slozky v /zip adresari aplikace, pak odeslat na web
    if os.path.exists(folder):
        if name.endswith(".zip"):
            zip_folder(folder, name)
        else:
            name = name + ".zip"
            zip_folder(folder, name)
            data = {
                'name': name
                }
            files = {
                'zipfile': (name, open(name, 'rb'), 'application/zip')
                }
            
            if LOCAL:
                url = "http://127.0.0.1:5000/add-tool"
            else:
                url = URL + "add-tool"
            response = requests.post(url=url, data=data, files=files)
            print('Status code: ', response.status_code)
            print('Server response: ', response.text)

        requests.put()
    if False:
        url = URL + "add-tool"
        requests.put(url)
    pass

def run(app):
    try:
        os.system(os.path.join(app, "main.exe"))
    except Exception as e:
        print("Error when trying to run application: ", e)