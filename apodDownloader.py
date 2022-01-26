#!/usr/bin/env python3
import os
import os.path
import requests
import urllib.request
from dotenv import load_dotenv
import datetime
load_dotenv()
apiKey = os.getenv("API_KEY")

url = f"https://api.nasa.gov/planetary/apod?api_key={apiKey}" 
r = requests.get(url).json()
image = r["hdurl"]
today = datetime.datetime.now().strftime('%Y-%m-%d')

home = os.path.expanduser("~")
dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(home,dir)
imageName = f"apod_{today}.jpg"
filename = os.path.join(path,imageName)

print(filename)
#urllib.request.urlretrieve(image, filename)

