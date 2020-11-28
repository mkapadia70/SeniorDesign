import PortsHandler
import SerialHandler
import JsonHandler
import time
from Apps import WindowsVolumeMixerControl

emulation = True  # enable this when using emulation
rasp = not emulation

if rasp:
    inport = 3
    outport = 3
else:
    inport = 4  # change this according to your in and out com ports as set by com0com
    outport = 5


def main():
    port = PortsHandler.checkConnected(inport)
    while port is None:
        print("Device Not Found")
        port = PortsHandler.findPort()
        time.sleep(10)
    print("Device has been found on port", port)
    s = SerialHandler.connectPort(port)

    # The listen will infinite loop in the handler
    SerialHandler.listen(s)


if __name__ == '__main__':
    main()
