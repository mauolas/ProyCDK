#!/bin/python3

from flask import Flask, request
import controller
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/saludo/<persona>')
def hello(persona):
    return 'Hello, ' + persona

@app.route('/rlineal', methods=['POST','GET'])
def preRLinea():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        vx = data['vx']
        vy = data['vy']
        x = data['x']
        #return "y_obj: " + str(controller.getRLineal(vx, vy, x))
        return controller.getRLineal(vx, vy, x)
    else:
        return "not found"

@app.route('/session', methods=['POST'])
def getsess():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        email = data['email']
        passw = data['password']
        return controller.getSession(email,passw)
    return

