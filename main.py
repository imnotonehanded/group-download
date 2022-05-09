from sqlite3 import Cursor
import urllib.request  # the lib that handles the url stuff
import xml.etree.ElementTree as ET
import re
import requests
import os
import colorama
import time

def watermark():
    print("""                                                                                                                    
                                                                                                                    
 $$$$$$\   $$$$$$\   $$$$$$\  $$\   $$\  $$$$$$\         $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\  
$$  __$$\ $$  __$$\ $$  __$$\ $$ |  $$ |$$  __$$\       $$  __$$\ $$  __$$\  \____$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
$$ /  $$ |$$ |  \__|$$ /  $$ |$$ |  $$ |$$ /  $$ |      $$ |  \__|$$$$$$$$ | $$$$$$$ |$$ /  $$ |$$$$$$$$ |$$ |  \__|
$$ |  $$ |$$ |      $$ |  $$ |$$ |  $$ |$$ |  $$ |      $$ |      $$   ____|$$  __$$ |$$ |  $$ |$$   ____|$$ |      
\$$$$$$$ |$$ |      \$$$$$$  |\$$$$$$  |$$$$$$$  |      $$ |      \$$$$$$$\ \$$$$$$$ |$$$$$$$  |\$$$$$$$\ $$ |      
 \____$$ |\__|       \______/  \______/ $$  ____/       \__|       \_______| \_______|$$  ____/  \_______|\__|      
$$\   $$ |                              $$ |                                          $$ |                          
\$$$$$$  |                              $$ |                                          $$ |                          
 \______/                               \__|                                          \__|                          \n\n""")


def eligble(filename):
    return "".join([c for c in filename if c.isalpha() or c.isdigit() or c==' ']).rstrip()


def getShirt(id):
    fr= requests.get(f'https://assetdelivery.roblox.com/v1/asset/?id={id}')
    for line in re.findall(r'(https?://[^\s]+)', fr.text):
        try:
            if line[0:31] == "http://www.roblox.com/asset/?id":
                assetID = line[32::].replace("</url>", "")
                nm = eligble(requests.get(f'http://api.roblox.com/Marketplace/ProductInfo?assetId={assetID}').json()[
                    'Name'])
                file = open( nm+".png", "x")
                urllib.request.urlretrieve(f'https://assetdelivery.roblox.com/v1/asset/?id={assetID}', os.path.realpath(file.name))
                print(colorama.Fore.GREEN+"[*] Downloaded!")
                file.close
        except Exception as e:
            print(e)
            continue

def loopPage(id, cursor):
    if cursor == None:
        for i in requests.get(f"https://catalog.roblox.com/v1/search/items/details?Category=3&CreatorType=2&IncludeNotForSale=true&Limit=30&CreatorTargetId={id}").json()["data"]:
            #4 requests
            getShirt(i["id"])
            time.sleep(0.332)
    else:
        for i in requests.get(f"https://catalog.roblox.com/v1/search/items/details?Category=3&CreatorType=2&IncludeNotForSale=true&Limit=30&CreatorTargetId={id}&cursor={cursor}").json()["data"]:
            #4 requests
            getShirt(i["id"])
            time.sleep(0.332)


def start():

    watermark()
    print("\n\n[1] Download Whole Group\n[2] Download Individual Clothing\n[3] Download List of Clothing")
    choice = input("Enter Choice: ")
    if choice == "1":
        os.system("cls")
        watermark()
        groupID = input("Enter Group ID: ")
        while True:
            cursorret = loopPage(groupID, None)
            if cursorret:
                cursor = cursorret
            else:
                break

    elif choice == "2":
        os.system("cls")
        watermark()
        getShirt(input("Enter Clothing ID: "))


start()
