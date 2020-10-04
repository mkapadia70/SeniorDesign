#!/user/bin/env python
import time
import serial
import json
from sys import argv

ser = serial.Serial(
    port='COM5', # for emulation insert your COMX port here
    #port='/dev/ttys0',
    baudrate = 20000,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

def Testing(tfval):
	
    try:
        
        test = ""

        if tfval == "false":
            test = [{"Name": "WindowsVolumeMixerControl","Funcs":[{"Name":"muteMasterVolume"}]}]
        elif tfval == "true":
            test = [{"Name": "WindowsVolumeMixerControl","Funcs":[{"Name":"unmuteMasterVolume"}]}]
           
        output = (json.dumps(test) + '\n').encode()
        ser.write(output)
        return output

    except Exception as e:
        print(e)
        return "a"

if __name__ == '__main__':
    print(Testing(argv[1]))

