from flask import Flask , render_template
from random import randint
import time
from pymongo import MongoClient
from json import dumps


app = Flask(__name__)
client = MongoClient('mongodb://root:rootpassword@mongodb:27017/admin')
collection = client.logdb.logcln

@app.route('/data')
def data():
    dblist = []
    startEpoch = int(time.time()-3600)
    for obj in collection.find({"timestamp": {"$gte": str(startEpoch) }}, {'_id': False }):
        if obj not in dblist:
            dblist.append(obj)
    return dumps(dblist).encode('utf-8')

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@app.route('/')
def index():
    return "" 

@app.route('/get', methods=['GET'])
def get():
    log("GET")
    return ""

@app.route('/post', methods=['POST'])
def post():
    log("POST")
    return ""

@app.route('/put', methods=['PUT'])
def put():
    log("PUT")
    return ""

@app.route('/delete', methods=['DELETE'])
def delete():
    log("DELETE")
    return ""

def log(request):
    response_time = randint(0,3000)
    time.sleep(response_time/1000)
    with open("log/log.txt", "a") as logfile:
        logfile.write(request + "," + str(response_time) + "," + str(int(time.time())) + "\n")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)
