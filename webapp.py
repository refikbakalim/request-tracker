from flask import Flask, render_template, request
import random
import time
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return "index" 

@app.route('/get', methods=['GET'])
def get():
    sleep("GET")
    return ""

@app.route('/post', methods=['POST'])
def post():
    sleep("POST")
    return ""

@app.route('/put', methods=['PUT'])
def put():
    sleep("PUT")
    return ""

@app.route('/delete', methods=['DELETE'])
def delete():
    sleep("DELETE")
    return ""

def sleep(request):
    response_time = random.randint(0,3000)
    time.sleep(response_time/1000)
    with open("logfile.txt", "a") as logfile:
        logfile.write(request + "," + str(response_time) + "," + str(int(time.time())) + "\n")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")