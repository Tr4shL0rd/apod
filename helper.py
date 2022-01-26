
import requests

def apikeyFound(apiKey) -> bool:
    if apiKey == None:
        return False
    else:
        return True

def verifyApiKey(apiKey):
    url = f"https://api.nasa.gov/planetary/apod?api_key={apiKey}"
    status = requests.get(url)
    if b'{\n  "error": {\n    "code": "API_KEY_INVALID",' in status.content:
        return False
    return True
