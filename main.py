import os
import requests

def get_list_of_tools():
    return requests.get("apt.pythonanywhere.com")