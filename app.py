
import json
from flask import Flask,jsonify
from requests import request
import module_temp as mt

app = Flask(__name__)


@app.route('/prova')
def helloworld():
    return jsonify({"about": " Helloworld !"})

@app.route('/temp', methods=['GET', 'POST'] )   #rotta per la get delle temperature
def get_temp():
    # if (request.method == 'GET'):             -- controllare perchè non funziona if 
        json_temps = json.dumps(mt.get_temps())   # dump della lista delle temperature presa in module_temp.py
        return json_temps

@app.route('/temp1', methods=['GET'])
def get_temp1():
    json_temps = json.dumps(mt.get_temps1())
    return (json_temps)

@app.route('/temp2', methods=['GET'])
def get_temp2():
    json_temps = json.dumps(mt.get_temps2())
    return (json_temps)

@app.route('/temp3', methods=['GET'])
def get_temp3():
    json_temps = json.dumps(mt.get_temps3())
    return (json_temps)

@app.route('/temp4', methods=['GET'])
def get_temp4():
    json_temps = json.dumps(mt.get_temps4())
    return (json_temps)


 

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)