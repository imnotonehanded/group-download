import urllib.request  # the lib that handles the url stuff
import xml.etree.ElementTree as ET
import re
import requests
import os
import colorama
from colour import Color
def find(string):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex, string)
    return [x[0] for x in url]

def get_rainbow_colors(length):
    """ Makes a list of rainbow Colors. """
    return [
        Color(hue=i/(length - 1), saturation=1, luminance=0.5)
        for i in range(length)]


def convert_to_hex_colors(colors):
    """ Convert a list of Color objects to hexadecimal colors. """
    return [color.get_hex_l() for color in colors]

def convert_to_rainbow_html_string(word):
    """ Returns a HTML text where the colors of the characters make a rainbow. """
    rainbow_colors = get_rainbow_colors(len(word))
    rainbow_colors = convert_to_hex_colors(rainbow_colors)
    html_str = ''
    for color, character in zip(rainbow_colors, word):
        html_str += '<font color="' + color + '">' + character + '</font>'

    return html_str


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
        line.decode('iso8859-1')
        try:
            if find(line.decode('iso8859-1'))[0][0:32] == "http://www.roblox.com/asset/?id=":
                file = open(requests.get(f'http://api.roblox.com/Marketplace/ProductInfo?assetId={id}').json()[
                                'Name'] + ".png", "x")
                urllib.request.urlretrieve(
                    'https://assetdelivery.roblox.com/v1/asset/?id={}'.format(find(line.decode('iso8859-1'))[0][32::]),
                    os.path.realpath(file.name))
                print(colorama.Fore.GREEN+"[*] Downloaded!")
        except Exception as e:
            continue

def start():
    print("""                                                                                                                    
                                                                                                                    
 $$$$$$\   $$$$$$\   $$$$$$\  $$\   $$\  $$$$$$\         $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\  
$$  __$$\ $$  __$$\ $$  __$$\ $$ |  $$ |$$  __$$\       $$  __$$\ $$  __$$\  \____$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
$$ /  $$ |$$ |  \__|$$ /  $$ |$$ |  $$ |$$ /  $$ |      $$ |  \__|$$$$$$$$ | $$$$$$$ |$$ /  $$ |$$$$$$$$ |$$ |  \__|
$$ |  $$ |$$ |      $$ |  $$ |$$ |  $$ |$$ |  $$ |      $$ |      $$   ____|$$  __$$ |$$ |  $$ |$$   ____|$$ |      
\$$$$$$$ |$$ |      \$$$$$$  |\$$$$$$  |$$$$$$$  |      $$ |      \$$$$$$$\ \$$$$$$$ |$$$$$$$  |\$$$$$$$\ $$ |      
 \____$$ |\__|       \______/  \______/ $$  ____/       \__|       \_______| \_______|$$  ____/  \_______|\__|      
$$\   $$ |                              $$ |                                          $$ |                          
\$$$$$$  |                              $$ |                                          $$ |                          
 \______/                               \__|                                          \__|                          """)

    print("\n\n[1] Download Whole Group\n[2] Download Individual Clothing\n[3] Download List of Clothing")
    choice = input("Enter Choice: ")

start()