import sys
from flask import Flask, jsonify, request
from flask_cors import cross_origin
from urllib.parse import urlparse
import time
import serial
import json

app = Flask(__name__)


def testing(params):
    funcName = "updateAudio"
    try:
        jason = ""
        if funcName == "muteUnmute":
            muted = params[1]
            if muted == "false":
                jason = [{"Name": "WindowsVolumeMixerControl","Funcs":[{"Name":"muteMasterVolume"}]}]
            elif muted == "true":
                jason = [{"Name": "WindowsVolumeMixerControl","Funcs":[{"Name":"unmuteMasterVolume"}]}]
        elif funcName == "updateAudio":
            volume = float(params)/100.0
            jason = [{"Name": "WindowsVolumeMixerControl","Funcs":[{"Name":"setMasterVolume", "Params": [volume]}]}]
        output = (json.dumps(jason) + '\n').encode()
        ser.write(output)
        return output
    except Exception as e:
        print(e)
        return "a"

@app.route("/data")
def data():
    
    content = request.args
    name = request.args.get('Name')
    funcs = request.args.get('Func')
    params = request.args.get("Params")
    processId = request.args.get("ProcessId")
    #funcs = [{"Name":"setMasterVolume", "Params": [volume]}]
    jason = [{"Name": name,"Funcs":[{"Name":funcs, "Params":[params, processId]}]}]
    #jason = [{'Name' : name, 'Funcs' : funcs}]
    output = (json.dumps(jason) + '\n').encode()
    ser.write(output)
    return jsonify(request.args)

if __name__ == "__main__":
    print('starting server')
    ser = serial.Serial(
        port='COM5', # for emulation insert your COMX port here
        #port='/dev/ttys0',
        baudrate = 100000,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )
    app.run(host='127.0.0.1', port=5001)