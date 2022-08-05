
import json
from flask import Flask,jsonify
from requests import request
import module_temp as mt

app = Flask(__name__)

@app.route('/prova')
def helloworld():
    return jsonify({"about": " Helloworld !"})

@app.route('/temp', methods=['GET'])   #rotta per la get delle temperature
def get_temp(): 
    json_temps = json.dumps(mt.get_temps())   # dump della lista delle temperature presa in module_temp.py
    return json_temps

@app.route('/temp/<int:id_sensore>', methods=['GET', 'POST'])
def get_temp_id(id_sensore):
    if((id_sensore>4) or (id_sensore<1)):
        return ("Errore: ID sensore non presente!")
    else:
        json_temps = mt.get_temps()
        chiave = "T" + str(id_sensore)
        temp = json_temps[chiave]
    
    return (json.dumps("T" + str(id_sensore) + "=" + str(temp)))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)