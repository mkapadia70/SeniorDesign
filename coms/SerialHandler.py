import serial
import json
import JsonHandler
import time
import sys
import serial.tools.list_ports

# SerialHandler.py
# this file handles sending/receiving data between pc and the device

ser = None


def checkConnected(port):
    # checks whether a device on the port exists on the windows machine
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if p.device == port:
            return True
    return False


def connectPort(port):
    # creates a serial connection
    global ser
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
    jason = (json.dumps(data) + '\n') # this takes a long time for large data
    send = jason.encode()
    ser.write(send)
    

def listen(ser1, ser2):
    # main listen loop for incoming messages from the device
    while 1:
        try:
            response = ser1.readline().decode()
            response = json.loads(response)
            print(response)
            data = JsonHandler.callFunctions(response) # call a function based on the response from the device
            if data != None: # send data back to the device if the function called had a return
                sendData(ser2, data)
        except Exception as e:
            pass


def clearBuffer():
    # flush the poop
    global ser
    if (ser != None):
        ser.reset_output_buffer() # clear buffer
        ser.reset_input_buffer() #clear buffer
        ser.flush()
    else:
        #print("none")
        return
