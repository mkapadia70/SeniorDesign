import sys
from flask import Flask, jsonify, request, render_template
from flask_cors import cross_origin
from urllib.parse import urlparse
import time
import serial
import json
from threading import Thread
import PortsHandler
import SerialHandler

emulation = True  # enable this when using emulation
rasp = not emulation

if rasp:
    inport = "/dev/ttys0"
    outport = "/dev/ttys0"
else:
    inport = "COM5"  # change this according to your in and out com ports as set by com0com
    outport = "COM7"

app = Flask(__name__)


def startServer():
    app.run(host='127.0.0.1', port=5001)


def listen():
    while 1:
        try:
            start = time.time()
            response = ser2.readline().decode(errors="replace")
            programData = json.loads(response)
            return programData
        except Exception as e:
            pass


def echo():
    # request to get program data from windows
    jason = [{"Name": "WindowsVolumeMixerControl", "Funcs": [
        {"Name": "getAllSoundDeviceData", "Params": ["1", "2"]}]}]
    output = (json.dumps(jason) + '\n').encode()
    ser1.write(output)


@app.route('/data2')
def hello():
    return jsonify(listen())


@app.route("/data")
def data():

    content = request.args
    name = request.args.get('Name')
    funcs = request.args.get('Func')
    params = request.args.get("Params")
    processId = request.args.get("ProcessId")

    jason = [{"Name": name, "Funcs": [
        {"Name": funcs, "Params": [params, processId]}]}]

    output = (json.dumps(jason) + '\n').encode()
    ser1.write(output)

    return jsonify(request.args)


if __name__ == "__main__":
    print('starting server')
    while (not PortsHandler.checkConnected(inport) or not PortsHandler.checkConnected(outport)):
        print("Device Not Found")
        time.sleep(5)

    print("In device has been found on port", inport)
    print("Out device has been found on port", outport)

    ser1 = SerialHandler.connectPort(inport)
    if rasp:
        ser2 = ser1
    else:
        ser2 = SerialHandler.connectPort(outport)

    Thread(target=startServer).start()
    Thread(target=echo).start()
