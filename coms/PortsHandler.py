import serial.tools.list_ports

def getCOMPort():
    piPort = emuPort = None

    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if ('Prolific USB-to-Serial Comm Port' in p.description):
            piPort = p.device
        if ('com0com' in p.description):
            emuPort = p.device
    if (piPort != None):
        return piPort
    return emuPort

def checkConnected():
    ports = list(serial.tools.list_ports.comports())

    for p in ports:
        if (("Prolific USB-to-Serial Comm Port" or "com0com") in p.description):
            return True

    return False
