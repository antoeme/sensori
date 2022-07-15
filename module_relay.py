from cgitb import text
from bs4 import BeautifulSoup
import requests


#url = "StatusTemperature.html"
with open("StatusRelays.html","r") as f:
    doc = BeautifulSoup(f,"html.parser")

#result = requests.get(url)

#print(doc.prettify())
tags = doc.find_all("span")

tags[0].string= "0"
print(tags[0].string)



