from multiprocessing import Process

from readSerialData import readSerialData
from writeSerialData import writeSerialData

# For the purposes of testing with emulation, 
# this program will run the read and write processes at the same time

def runInParallel(*fns):
  proc = []
  for fn in fns:
    p = Process(target=fn)
    p.start()
    proc.append(p)
  for p in proc:
    p.join()

def mainWindows():
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
    runInParallel(mainWindows, mainDevice)