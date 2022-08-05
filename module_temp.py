#modulo per il parsing html delle temperature

from time import sleep
from bs4 import BeautifulSoup
import requests
from os import getenv

num_sensori = getenv("num_sensori") or 4
url_sensori = getenv("url_sensori") or "http://10.10.10.81"

def get_temps():
    result = requests.get(url_sensori)
    doc = BeautifulSoup(result.text,"html.parser")  #passiamo result.text preso dalla get all'url dei sensori
    tags = doc.find_all(class_ = "temp" )

    temps= {}

    if(len(tags)) == 0:
        return temps

    for l in range(len(tags)):
        t = tags[l].string
        if(t!="---"):
            temps["T"+ str(l+1)] = float(t)
        else:
            temps["T"+ str(l+1)] = 0
    return temps


print(get_temps())


