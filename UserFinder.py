import random
import requests
import json
import time
CHARACTERS = "abcdefghijklmnopqrstuvwxyz1234567890-_"
#CHARACTERS[random.randint(0,63)]
#https://www.reddit.com/api/username_available.json?user=USER
while(True):
    USER = CHARACTERS[random.randint(0,37)] + CHARACTERS[random.randint(0,37)] + CHARACTERS[random.randint(0,37)] + CHARACTERS[random.randint(0,37)]
    URL = "https://www.reddit.com/api/username_available.json?user=" + USER
    #print(URL)
    isAvailable = requests.get(URL, headers = {'User-agent': 'Usernamechecker4'})
    isAvailable = json.loads(isAvailable.text)
    #print(isAvailable)
    if (isAvailable == True):
        usernames = open("./usernames.txt","a")
        usernames.write(USER+"\n")
        usernames.close()
