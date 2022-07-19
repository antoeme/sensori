
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
        json_temps = json.dumps(mt.temps)   # dump della lista delle temperature presa in module_temp.py
        return json_temps
 

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)