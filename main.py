import urllib.request  # the lib that handles the url stuff
import xml.etree.ElementTree as ET
import re
import requests
import os
import colorama
ID = input("Enter ID: ")
# root = ET.fromstring(country_data_as_string)
def Find(string):
    # findall() has been used
    # with valid conditions for urls in string
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex, string)
    return [x[0] for x in url]


def deEmojify(text):
    regrex_pattern = re.compile(pattern="["
                                        u"\U0001F600-\U0001F64F"  # emoticons
                                        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                        u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                        "]+", flags=re.UNICODE)
    return regrex_pattern.sub(r'', text)


# file = open('shirt.png', 'x')
for line in urllib.request.urlopen('https://assetdelivery.roblox.com/v1/asset/?id={}'.format(ID)):
    # if str(line).find("<url>http://www.roblox.com/asset/?id="):
    # print(Find(line.decode('iso8859-1'))[0][0:34])
    line.decode('iso8859-1')
    try:

        #print(Find(line.decode('iso8859-1')))
        if Find(line.decode('iso8859-1'))[0][0:32] == "http://www.roblox.com/asset/?id=":
            # print("done1")
            file = open(requests.get('http://api.roblox.com/Marketplace/ProductInfo?assetId={}'.format(ID)).json()[
                            'Name'] + ".png", "x")
            # file = open('shirt.png', 'x')
            # print(file.name+" file")
            urllib.request.urlretrieve(
                'https://assetdelivery.roblox.com/v1/asset/?id={}'.format(Find(line.decode('iso8859-1'))[0][32::]),
                os.path.realpath(file.name))
            print(colorama.Fore.GREEN+"[*] Downloaded!")
            # print(Find(line.decode('iso8859-1'))[0][32::])
    except Exception as e:
        #print(e
        continue
    # print(line.decode('iso8859-1')[line.decode('iso8859-1').find("<url>http://www.roblox.com/asset/?id=")::])
