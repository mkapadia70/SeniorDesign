import serial.tools.list_ports


def findPort():
    ports = list(serial.tools.list_ports.comports())
    port = None
    for p in ports:
        if (("Prolific USB-to-Serial Comm Port" in p.description) or ("com0com" in p.description)):
            port = p.device
            return port
        
