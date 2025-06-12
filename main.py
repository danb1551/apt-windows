import os
import requests
import json
import sys
import lib


def main(args):
    missed = True
    cont = True # continue
    if len(args) == 1:
        print("Why are you running it without commands?!")
        exit(0)
    for i in range(len(args)):
        act_arg = args[i].lower() # name like 'actual arguments' (for dumb)
        if act_arg == "install":
            cont = False
            try:
                package_for_inst = args[i+1]
            except Exception as e:
                package_for_inst = None
                print("Error when trying to get package for installation: ", e)
                break
            missed = False
            lib.install_package(package_for_inst)
        elif act_arg == "deploy":
            cont = False
            try:
                folder = args[i+1]
                name = args[i+2]
                author = args[i+3]
            except Exception as e:
                package_for_inst = None
                print("Error when trying to get package for deploy: ", e)
                break
            try:
                missed = False
                lib.deploy(folder, name, author)
            except Exception as e:
                print("Error when trying to deploy it to the server", e)
                break
        elif act_arg in os.listdir("C:\\wapt\\"):
            cont = False
            lib.run(act_arg)
            missed = False
    if missed == True:
        print("Sorry bro, you missed")
        exit(0)

if __name__ == "__main__":
    if not os.path.exists("C:\\wapt\\"):
        os.mkdir("C:\\wapt\\")
    main(args=sys.argv)