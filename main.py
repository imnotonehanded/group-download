import urllib.request  # the lib that handles the url stuff
import xml.etree.ElementTree as ET
import re
import requests
import os
import colorama


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
    fr= requests.get(f'https://assetdelivery.roblox.com/v1/asset/?id={id}')
#print(fr.text)
for line in re.findall(r'(https?://[^\s]+)', fr.text):
        try:
            if line[0:31] == "http://www.roblox.com/asset/?id":
                assetID = line[32::].replace("</url>", "")
                file = open(requests.get(f'http://api.roblox.com/Marketplace/ProductInfo?assetId={assetID}').json()[
                    'Name'] + ".png", "x")
                file.write(requests.get(f'https://assetdelivery.roblox.com/v1/asset/?id={assetID}').text)
                print(colorama.Fore.GREEN+"[*] Downloaded!")
        except Exception as e:
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
