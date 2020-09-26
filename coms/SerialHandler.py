import serial
import json

s = None

def connectPort(port):
    s = serial.Serial(
        port=port,
        baudrate=20000,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1)

def sendData(data):
    data = (json.dumps(my_arr) + '\n').encode()
    s.write(data)

def listen():
    while 1:
        try:
            response = s.readline().decode(errors="replace")
            response = json.loads(response)
        except:
            print("Timed out")

    return response
