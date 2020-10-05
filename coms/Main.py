import PortsHandler
import SerialHandler
import JsonHandler
import time
from Apps import WindowsVolumeMixerControl

def main():
    
    print("Device Not Found")
    port = None
    port = PortsHandler.findPort()
    while(None == port):
        port = PortsHandler.findPort()
        time.sleep(10)
    print("Device has been found on port", port)
    s = SerialHandler.connectPort(port)
    
    # The listen will infinite loop in the handler
    SerialHandler.listen(s)
        
if __name__ == '__main__':
    main()
