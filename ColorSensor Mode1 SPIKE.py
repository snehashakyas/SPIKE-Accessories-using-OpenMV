import hub
import time
hub.port.C.mode(hub.port.MODE_FULL_DUPLEX) # OpenMV connected to Port C in SPIKE.
hub.port.C.baud(9600)

a = hub.port.C.read(10) # To discard first read value, which is always '\xff'.

while True:   
    a = hub.port.C.read(10)
    if(len(a) != 0):
        print(a) # Prints out color detected on SPIKE.
    
    time.sleep(1)
