import os
import requests
import json
import sys

def get_list_of_tools(url: str = "http://127.0.0.1:5000/get-list"):
    return json.loads(requests.post(url).content.decode("utf-8"))

def main(args):
    print(args.install)
print(get_list_of_tools())
if __name__ == "__main__":
    print("Argumenty:", sys.argv)
    print("Název skriptu:", sys.argv[0])
    print("Zadané argumenty:", sys.argv[1:])