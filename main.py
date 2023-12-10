from sqlite3 import Cursor
from tokenize import group
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
    # checks if the filename can be made a file
    return "".join([c for c in filename if c.isalpha() or c.isdigit() or c==' ']).rstrip()


def getShirt(id, folder):
    #requests roblox api
    fr= requests.get(f'https://assetdelivery.roblox.com/v1/asset/?id={id}')
    for line in re.findall(r'(https?://[^\s]+)', fr.text):
        #finds all links
        #print(line)
        try:
            if line[0:31] == "http://www.roblox.com/asset/?id":
                assetID = line[32::].replace("</url>", "")
                print(assetID)
                #gets the asset id
                nm = eligble(requests.get(f'http://api.roblox.com/Marketplace/ProductInfo?assetId={assetID}').json()[
                    'Name'])
                #makes sure name isd valid
                print(nm)
                if folder != None:
                    #makes a folder if none
                    file = open(os.path.join(folder, nm+".png"), "x")
                else:
                    file = open(nm+".png", "x")
                urllib.request.urlretrieve(f'https://assetdelivery.roblox.com/v1/asset/?id={assetID}', os.path.realpath(file.name))
                #uses urllib to get the image of the shirt
                #print(colorama.Fore.GREEN+"[*] Downloaded!")
                file.close
        except Exception as e:
            print(e)
            continue

def loopPage(id, cursor, folder):
    #loops through the pages of api w cursor
    if cursor == None:
        nonCursor = requests.get(f"https://catalog.roblox.com/v1/search/items/details?Category=3&CreatorType=2&IncludeNotForSale=false&Limit=10&CreatorTargetId={id}").json()
        #checks if theres a cursor
        for i in nonCursor["data"]:
            #4 requests
            getShirt(i["id"], folder)
        if nonCursor["nextPageCursor"]:
            return nonCursor["nextPageCursor"]
        else: 
            return False
    else:
        #gets shirt with cursor
        yCursor = requests.get(f"https://catalog.roblox.com/v1/search/items/details?Category=3&CreatorType=2&IncludeNotForSale=false&Limit=10&CreatorTargetId={id}&cursor={cursor}").json()
        for j in yCursor["data"]:
            #4 requests
            print(j)
            getShirt(j["id"], folder)
        if yCursor["nextPageCursor"]:
            return yCursor["nextPageCursor"]
        else: 
            return False


def start():

    watermark()
    
    print("\n\n[1] Download Whole Group\n[2] Download Individual Clothing\n[3] Download List of Clothing")
    choice = input("Enter Choice: ")
    if choice == "1":
        os.system("cls")
        watermark()
        groupID = input("Enter Group ID: ")
        cursor = None
        folder = os.mkdir(str(groupID))
        while True:
            print(cursor)
            cursorret = loopPage(groupID, cursor, os.path.realpath(str(groupID)))
            if cursorret:
                print(cursor)
                cursor = cursorret
                print(cursor)
                time.sleep(0.022)
            else:
                break

    elif choice == "2":
        os.system("cls")
        watermark()
        getShirt(input("Enter Clothing ID: "), None)


#start()
getShirt("322436466", None)
