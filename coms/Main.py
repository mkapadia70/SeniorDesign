import SerialHandler
import JsonHandler
import time

# Main.py

emulation = True  # enable this when using emulation
rasp = not emulation

if rasp:
    inport = "COM3"
    outport = "COM3"
else:
    inport = "COM3"  # change this according to your in and out com ports as set by com0com
    outport = "COM5"


def main():
    # ensures a connected exists for both in and out ports
    while (not SerialHandler.checkConnected(inport) or not SerialHandler.checkConnected(outport)):
        print("Device Not Found")
        time.sleep(5)

    print("In device has been found on port", inport)
    print("Out device has been found on port", outport)

    # sets up connection objects for both in and out ports
    ser1 = SerialHandler.connectPort(inport)
    if rasp:
        ser2 = ser1
    else:
        ser2 = SerialHandler.connectPort(outport)

    JsonHandler.setupApps() # init various apps stuff

    # The listen will infinite loop in the handler
    SerialHandler.listen(ser1, ser2)


if __name__ == '__main__':
    main()
