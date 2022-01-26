#!/usr/bin/env python3
import os
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
path = "/home/tr4shl0rd/programmingLanguages/python/nasa/"
filename = f"{path}apod_{today}.jpg"

urllib.request.urlretrieve(image, filename)

