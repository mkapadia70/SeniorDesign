import serial.tools.list_ports

#note: should fix how this all does this. 
# Hopefully can do both of these in one function
# and not have to return to main until the end
def getCOMPort():
    piPort = emuPort = None

    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if ('Prolific USB-to-Serial Comm Port' in p.description):
            piPort = p.device
        elif ('com0com' in p.description):
            emuPort = p.device
    if (piPort != None):
        return piPort
    return emuPort

def checkConnected():
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if (("Prolific USB-to-Serial Comm Port" in p.description) or ("com0com" in p.description)):
            return True

    return False
