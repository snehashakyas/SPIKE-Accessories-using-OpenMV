import hub
import time
hub.port.C.mode(hub.port.MODE_FULL_DUPLEX)
hub.port.C.baud(9600)

while True:   
    a = hub.port.C.read(10)
    print(a) # Prints out color detected on SPIKE.
    
    time.sleep(1)
