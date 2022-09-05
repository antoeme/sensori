
import json
from flask import Flask,jsonify
from requests import request
from dotenv import load_dotenv
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from time import sleep
from bs4 import BeautifulSoup
import requests
from os import getenv

NUM_SENSORI = getenv("NUM_SENSORI") #or 4
URL_SENSORI = getenv("URL_SENSORI") #or "http://10.10.10.81"

# load environment variables from '.env' file
load_dotenv()

def get_temps():
    result = requests.get(str(URL_SENSORI))
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

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "daniele": generate_password_hash("Cisco123"),
    "antonio": generate_password_hash("Dtlab123")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username



@app.route('/temp', methods=['GET'])   #rotta per la get delle temperature
@auth.login_required
def get_temp(): 
    json_temps = json.dumps(get_temps())   # dump della lista delle temperature presa in module_temp.py
    return json_temps

@app.route('/temp/<int:id_sensore>', methods=['GET', 'POST'])
@auth.login_required
def get_temp_id(id_sensore):
    if((id_sensore>int(NUM_SENSORI)) or (id_sensore<1)):
        return ("Errore: ID sensore non presente!")
    else:
        json_temps = get_temps()
        chiave = "T" + str(id_sensore)
        temp = json_temps[chiave]
    
    return (json.dumps("T" + str(id_sensore) + "=" + str(temp)))

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', debug=True)