import serial
import json
s = serial.Serial(
    port='COM3',
    baudrate=20000,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1)

while 1:
    res = s.readline().decode(errors="ignore")
    # print(res, end='')
    parsed = json.loads(res)
    print(json.dumps(parsed, indent=4, sort_keys=True))
