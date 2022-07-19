
import json
from flask import Flask,jsonify
from redis import Redis
from requests import request
import module_temp as mt

app = Flask(__name__)
redis = Redis(host='redis',port=6379)

# @app.route('/')
# def hello():
#     redis.incr('hits')
#     counter=str(redis.get('hits'), 'utf-8')
#     return 'Welcome, this page has been viewed '+ counter+'time(s)'

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