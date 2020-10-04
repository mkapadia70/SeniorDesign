import serial
import json
import JsonHandler
import time

s = None

def connectPort(port):
    s = serial.Serial(
        port=port,
        baudrate=20000,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1)
    return s

def sendData(data):
    data = (json.dumps(data) + '\n').encode()
    s.write(data)

def listen(ser):
    while 1:
        try:
            response = ser.readline().decode(errors="replace")
            response = json.loads(response)
            print(response)
            JsonHandler.callFunctions(response)
        except Exception as e:
            pass

    return response
