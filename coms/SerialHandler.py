import serial
import json
import JsonHandler
import time
import sys


def connectPort(port):
    # the main serial connection
    ser = serial.Serial(
        port=port,
        baudrate=115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1)
    ser.set_buffer_size(rx_size = 115200, tx_size = 115200)
    return ser

def sendData(ser, data):
    ser.reset_output_buffer() # clear buffer
    jason = (json.dumps(data) + '\n') # this takes a long time
    send = jason.encode()
    ser.write(send)
    ser.reset_output_buffer() # clear buffer, gotta flush after you poop
    ser.flush()

def listen(ser1, ser2):
    JsonHandler.updateDevices()
    while 1:
        try:
            response = ser1.readline().decode()
            response = json.loads(response)
            print(response)
            data = JsonHandler.callFunctions(response)
            if data != None:
                print("here before send")
                sendData(ser2, data)
        except Exception as e:
            pass
