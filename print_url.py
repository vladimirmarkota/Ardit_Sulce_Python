import requests

r = requests.get("https://pythonhow.com/media/data/universe.txt")
print(r.text)

