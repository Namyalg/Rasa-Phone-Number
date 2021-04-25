import requests
import json


resp = requests.get("https://68b28f8406ad.ngrok.io/218")

resp = json.loads(resp.text)
print(resp["Present"])
