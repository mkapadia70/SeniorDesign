import serial
import json
import JsonHandler
import time

def connectPort(port):
    return serial.Serial(
        port=port,
        baudrate=100000,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1)

def sendData(ser, data):
    ser2 = serial.Serial(
        port='COM8', # for emulation insert your COMX port here
        #port='/dev/ttys0',
        baudrate = 100000,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )
    data = (json.dumps(data) + '\n').encode()
    ser2.write(data)

def listen(ser):
    JsonHandler.updateDevices()
    while 1:
        try:
            response = ser.readline().decode(errors="replace")
            response = json.loads(response)
            #print(response)
            data = JsonHandler.callFunctions(response)
            if data != None:
                sendData(ser, data)
        except Exception as e:
            pass