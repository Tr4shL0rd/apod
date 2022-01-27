#!/usr/bin/env python3
import os
import os.path
import requests
import urllib.request
from dotenv import load_dotenv
import datetime
import helper
import json

load_dotenv()
apiKey = os.getenv("API_KEY")


# checks if apikey is valid
if helper.apikeyFound(apiKey) == False:
    if json.load(open("data.json"))["API_KEY"] == None:
        print("API key not found")
        print("Please generate an api key here: https://api.nasa.gov/")
        apiKeyInput = input("Enter your API key: ")
        if helper.verifyApiKey(apiKeyInput) == False:
            print("Invalid API key")
        else:
            with open("data.json", "w") as f:
                json.dump({"API_KEY": apiKeyInput}, f)
            apiKey = json.load(open("data.json"))["API_KEY"]
    else:
        apiKey = json.load(open("data.json"))["API_KEY"]
helper.verifyApiKey(apiKey)
url = f"https://api.nasa.gov/planetary/apod?api_key={apiKey}" 

#fetches the data from the api and parses it into a dictionary
r = requests.get(url).json()
#gets hd image
image = r["hdurl"]

today = datetime.datetime.now().strftime('%Y-%m-%d')
#gets current directory and creates a file in that directory with a name of today's date
home = os.path.expanduser("~")
dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(home,dir)
imageName = f"apod_{today}.jpg"
filename = os.path.join(path,imageName)

#downloads the image
urllib.request.urlretrieve(image, filename)
print(f"saved to {filename}")
helper.setwallpaper(filename)
