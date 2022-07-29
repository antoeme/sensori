#modulo per il parsing html delle temperature

from time import sleep
from bs4 import BeautifulSoup
import requests
from os import getenv

num_sensori = getenv("num_sensori") or 4
url_sensori = getenv("url_sensori") or "http://10.10.10.81"
# num_sensori = 4 
# url_sensori = "http://10.10.10.81"

# with open("StatusTemperature.html","r") as f:
#     doc = BeautifulSoup(f,"html.parser")

def get_temps():
    result = requests.get(url_sensori)
    doc = BeautifulSoup(result.text,"html.parser")  #passiamo result.text preso dalla get all'url dei sensori
    # print(doc)
    tags = doc.find_all(class_ = "temp" )

    #print (tags)
    temps= {}

    for l in range(len(tags)):
        t = tags[l].string
        if(t!="---"):
            temps["T"+ str(l+1)] = float(t)
        else:
            temps["T"+ str(l+1)] = 0
    return temps

def get_temps1():
    result = requests.get(url_sensori)
    doc = BeautifulSoup(result.text,"html.parser")  #passiamo result.text preso dalla get all'url dei sensori
    
    tags = doc.find(id = 'divT1')

    tags = tags.string

    if (tags == "---"):
        tags = 0
    
    return tags

def get_temps2():
    result = requests.get(url_sensori)
    doc = BeautifulSoup(result.text,"html.parser")  #passiamo result.text preso dalla get all'url dei sensori
    
    tags = doc.find(id = 'divT2')
    
    tags = tags.string

    if (tags == "---"):
        tags = 0
    
    return tags

def get_temps3():
    result = requests.get(url_sensori)
    doc = BeautifulSoup(result.text,"html.parser")  #passiamo result.text preso dalla get all'url dei sensori
    
    tags = doc.find(id = 'divT3')

    tags = tags.string

    if (tags == "---"):
        tags = 0
    
    return tags

def get_temps4():
    result = requests.get(url_sensori)
    doc = BeautifulSoup(result.text,"html.parser")  #passiamo result.text preso dalla get all'url dei sensori
    
    tags = doc.find(id = 'divT4')

    tags = tags.string
    
    if (tags == "---"):
        tags = 0
    
    return tags

print(get_temps())


