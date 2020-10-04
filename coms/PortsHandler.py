import serial.tools.list_ports

def checkConnected(port):
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if p.device == port:
            return True
    return False
        
    return port in list(serial.tools.list_ports.comports())

def findPort():
    ports = list(serial.tools.list_ports.comports())
    port = None
    for p in ports:
        if (("Prolific USB-to-Serial Comm Port" in p.description) or ("com0com" in p.description)):
            return p.device
        
