#modulo per il parsing html delle temperature

from cgitb import html, text
from unittest import result
from bs4 import BeautifulSoup
import requests


num_sensori = 4 
#url = "StatusTemperature.html"

#result = requests.get(url)
#print(result.text)

with open("StatusTemperature.html","r") as f:
    doc = BeautifulSoup(f,"html.parser")

#print(doc.prettify())

tags = doc.find_all(class_ = "temp" )
temps= []
for l in range(len(tags)):
    t = tags[l].string
    temps.append(t)
print(temps)

