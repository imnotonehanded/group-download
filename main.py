import urllib.request  # the lib that handles the url stuff
import xml.etree.ElementTree as ET
import re
import requests
import os
import colorama


def find(string):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex, string)
    return [x[0] for x in url]


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


def deEmojify(text):
    regrex_pattern = re.compile(pattern="["
                                        u"\U0001F600-\U0001F64F"  # emoticons
                                        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                        u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                        "]+", flags=re.UNICODE)
    return regrex_pattern.sub(r'', text)


def getShirt(id):
    for line in urllib.request.urlopen(f'https://assetdelivery.roblox.com/v1/asset/?id={id}'):

        try:
            if find(line.decode('iso8859-1'))[0][0:32] == "http://www.roblox.com/asset/?id=":
                file = open(requests.get(f'http://api.roblox.com/Marketplace/ProductInfo?assetId={id}').json()[
                    'Name'] + ".png", "x")
                urllib.request.urlretrieve(
                    'https://assetdelivery.roblox.com/v1/asset/?id={}'.format(
                        find(line.decode('iso8859-1'))[0][32::]),
                    file)
                print(colorama.Fore.GREEN+"[*] Downloaded!")
        except Exception as e:
            print(e)
            continue



def start():

    watermark()
    print("\n\n[1] Download Whole Group\n[2] Download Individual Clothing\n[3] Download List of Clothing")
    choice = input("Enter Choice: ")
    if choice == "2":
        os.system("cls") or os.system("clear")
        watermark()
        getShirt(input("Enter Clothing ID: "))


start()
