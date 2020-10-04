import PortsHandler
import SerialHandler
import time

def main():
    running = True
    while(running):
        print("Device Not Found")
        port = None
        port = PortsHandler.findPort()
        while(None == port):
            port = PortsHandler.findPort()
            time.sleep(10)
        print("Device has been found on port", port)
        s = SerialHandler.connectPort(port)

        while(PortsHandler.checkConnected(port)):
            SerialHandler.listen(s)

if __name__ == '__main__':    
    main()
