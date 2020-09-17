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

if __name__ == '__main__':    
    runInParallel(readSerialData, writeSerialData)