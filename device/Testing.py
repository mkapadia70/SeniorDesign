#!/user/bin/env python
import time
import serial
import json
from sys import argv

ser = serial.Serial(
    port='/dev/ttyS0',
    baudrate = 20000,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

def Testing(tfval):
	"""based on the input text, return the operation result"""
	try:
	    
            
            test1 = [{"Name": "WindowsVolumeMixerControl","Funcs":[{"Name":"muteMasterVolume"}]}]
            test2 = [{"Name": "WindowsVolumeMixerControl","Funcs":[{"Name":"unmuteMasterVolume"}]}]

            output1 = (json.dumps(test1) + '\n').encode()
            output2 = (json.dumps(test2) + '\n').encode()


	    if tfval == "false":
		    print("here", tfval)
                    ser.write(output1)
		    return output1
            elif  tfval == "true":
	 	    print("there", tfval)
                    ser.write(output2)
		    return output2
                
	except Exception as e:
		print(e)
		return "a"




if __name__ == '__main__':
    print(Testing(argv[1]))

