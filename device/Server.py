import sys
from flask import Flask, jsonify, request
from flask_cors import cross_origin
from urllib.parse import urlparse
import time
import serial
import json
import SerialHandler

app = Flask(__name__)


@app.route("/data")
def data():
    
    content = request.args
    name = request.args.get('Name')
    funcs = request.args.get('Func')
    params = request.args.get("Params")
    processId = request.args.get("ProcessId")

    jason = [{"Name": name,"Funcs":[{"Name":funcs, "Params":[params, processId]}]}]

    output = (json.dumps(jason) + '\n').encode()
    ser1.write(output)

    return jsonify(request.args)

if __name__ == "__main__":
    print('starting server')
    ser1 = serial.Serial(
        port='COM5', # for emulation insert your COMX port here
        #port='/dev/ttys0',
        baudrate = 100000,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )
    app.run(host='127.0.0.1', port=5001)
    