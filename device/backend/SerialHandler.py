import serial
import json
import time

def connectPort(port):
    # the main serial connection
    return serial.Serial(
        port=port,
        baudrate=115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1)


def sendData(ser, data):
    ser.flush()  # flush buffer
    data = (json.dumps(data) + '\n').encode()
    ser.write(data)

def listen(ser):
    start = time.time()
        while time.time()-start < 10:
            try:
                start = time.time()
                response = ser.readline().decode(errors="replace")
                programData = json.loads(response)
                return programData
            except Exception as e:
                pass
