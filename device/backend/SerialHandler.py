import serial
import json
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
    jason = (json.dumps(data) + '\n') # this takes a long time
    send = jason.encode()
    ser.write(send)

def listen(ser):
    response = ""
    start = time.time()
    while time.time() - start < 10: # 2 second manual timeout on listen bc this is dumb
        try:
            response = ser.readline()
            deocoded = response.decode(errors="ignore")
            programData = json.loads(deocoded)
            ser.reset_input_buffer()
            return programData
        except Exception as e:
            print("hit listen error ", e, response, file=sys.stderr)
            ser.reset_output_buffer() # clear buffer
            ser.reset_input_buffer() #clear buffer
            ser.flush()
            ser.send_break()
            pass
    return None
