import requests

r = requests.get("http://www.pythonhow.com/data/universe.txt")
x = r.text
y = x.count("a")
print(y)


