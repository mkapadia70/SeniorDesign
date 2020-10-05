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

def Testing(params):
    funcName = params[0]
    try:
        jason = ""
        print(funcName)
        if funcName == "muteUnmute":
            muted = params[1]
            if muted == "false":
                jason = [{"Name": "WindowsVolumeMixerControl","Funcs":[{"Name":"muteMasterVolume"}]}]
            elif muted == "true":
                jason = [{"Name": "WindowsVolumeMixerControl","Funcs":[{"Name":"unmuteMasterVolume"}]}]
        elif funcName == "updateAudio":
            volume = float(str(params[1]))/100.0
            jason = [{"Name": "WindowsVolumeMixerControl","Funcs":[{"Name":"setMasterVolume", "Params": [volume]}]}]
        output = (json.dumps(jason) + '\n').encode()
        ser.write(output)
        return output


    except Exception as e:
        print(e)
        return "a"

if __name__ == '__main__':
    params = argv[1].split(',')
    print(Testing(params))

