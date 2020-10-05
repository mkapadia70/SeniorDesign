import serial
import json
import JsonHandler
import time
#clean this up at some point


def connectPort(port):
    return serial.Serial(
        port=port,
        baudrate=100000,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1)

def sendData(ser, data):
    data = (json.dumps(data) + '\n').encode()
    ser.write(data)

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
