import PortsHandler
import SerialHandler
import time

def main():
    running = True
    while(running):
        print("Device Not Found")
        while(not PortsHandler.checkConnected()):
            time.sleep(10)
        port = PortsHandler.getCOMPort()
        print("Device has been found on port", port)
        s = SerialHandler.connectPort(port)

        while(PortsHandler.checkConnected()):
            SerialHandler.listen(s)

if __name__ == '__main__':    
    main()
