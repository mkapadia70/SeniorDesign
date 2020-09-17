import serial.tools.list_ports


def getCOMPorts():
    ports = list(serial.tools.list_ports.comports())
    arduinoPorts = []
    emuPorts = []
    for p in ports:
        if 'Arduino' in p.description:
            arduinoPorts.append(p)
        if 'com0com' in p.description:
            emuPorts.append(p)
    return arduinoPorts, emuPorts
