import urllib.request  # the lib that handles the url stuff
import xml.etree.ElementTree as ET
import re
import requests
import os
import colorama
id = 478730838
def find(string):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex, string)
    return [x[0] for x in url]

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