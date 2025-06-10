import os
import requests
import json
import sys
import lib


def main(args):
    missed = True
    if len(args) == 1:
        print("Why are you running it without commands?!")
        exit(0)
    for i in range(len(args)):
        act_arg = args[i].lower() # name like 'actual arguments' (for dumb)
        if act_arg == "install":
            try:
                package_for_inst = args[i+1]
            except Exception as e:
                package_for_inst = None
                print("Error when trying to get package for installation: ", e)
                exit(0)
            missed = False
            lib.install_package(package_for_inst)
        elif missed == True:
            print("Sorry bro, you missed")
            exit(0)

if __name__ == "__main__":
    main(args=sys.argv)