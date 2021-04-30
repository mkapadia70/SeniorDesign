import sys
from flask import Flask, jsonify, request
from flask_cors import cross_origin
import time
import serial
import json
import SerialHandler

# Server.py
# this is an important 'middleman' program that 
# * handles REST calls to/from our electron app
# * handles serial connection (encoded json data) to/from our Windows device
# this program is launched by the electron app on startup

emulation = True  # True when using emulation, False otherwise
rasp = not emulation

if rasp:
    inport = "/dev/ttyS0"
    outport = "/dev/ttyS0"
else:
    inport = "COM4"  # change this according to your in and out com ports as set by com0com
    outport = "COM6"

app = Flask(__name__)


def startServer():
    app.run(host='127.0.0.1', port=5001)


@app.route("/data")
def data():

    content = request.args
    name = request.args.get('Name')
    funcs = request.args.get('Func')
    params = request.args.getlist("Params")
    expectReturn = request.args.get("ExpectReturn")

    packageAndSend(name, funcs, params)

    if expectReturn == "true":
        # this could probably be improved, but I dont wanna rn
        ret = SerialHandler.listen(ser2)
        return jsonify(ret)
    else:
        return jsonify(request.args)  # just bs value


def packageAndSend(name, funcs, params):

    # packages up everything and sends as generic request to Windows-side
    jason = [{"Name": name, "Funcs": [
        {"Name": funcs, "Params": params}]}]

    SerialHandler.sendData(ser1, jason)


if __name__ == "__main__":
    print('starting server')
    while (not SerialHandler.checkConnected(inport) or not SerialHandler.checkConnected(outport)):
        print("Device Not Found")
        time.sleep(5)

    print("In device has been found on port", inport)
    print("Out device has been found on port", outport)

    ser1 = SerialHandler.connectPort(inport)
    if rasp:
        ser2 = ser1
    else:
        ser2 = SerialHandler.connectPort(outport)

    startServer()
