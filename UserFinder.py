import random
import requests
import json
import time

CHARACTERS = "abcdefghijklmnopqrstuvwxyz1234567890-_"
LENGTH = len(CHARACTERS) - 1

# Start of loop
while(True):
    # Generate random 4 character string consisting of characters in CHARACTERS
    USER = CHARACTERS[random.randint(0, LENGTH)] + CHARACTERS[random.randint(0, LENGTH)] + CHARACTERS[random.randint(0, LENGTH)] + CHARACTERS[random.randint(0, LENGTH)]

    # Check username availability using Reddit API
    isAvailable = requests.get("https://www.reddit.com/api/username_available.json?user=" + USER, headers={'User-agent': 'Usernamechecker4'})
    isAvailable = json.loads(isAvailable.text)

    # Adds username to txt file if it is available
    if (isAvailable == True):
        usernames = open("./usernames.txt", "a")
        usernames.write(USER+"\n")
        usernames.close()