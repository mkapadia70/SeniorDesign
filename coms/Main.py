import PortsHandler
import SerialHandler
import JsonHandler
import time
from Apps import WindowsVolumeMixerControl

emulation = True  # enable this when using emulation
rasp = not emulation

if rasp:
    inport = "COM3"
    outport = "COM3"
else:
    inport = "COM4"  # change this according to your in and out com ports as set by com0com
    outport = "COM5"


def main():
    while (not PortsHandler.checkConnected(inport) or not PortsHandler.checkConnected(outport)):
        print("Device Not Found")
        time.sleep(5)

    print("In device has been found on port", inport)
    print("Out device has been found on port", outport)

    ser1 = SerialHandler.connectPort(inport)
    if rasp:
        ser2 = ser1
    else:
        ser2 = SerialHandler.connectPort(outport)

    # The listen will infinite loop in the handler
    SerialHandler.listen(ser1, ser2)


if __name__ == '__main__':
    main()
