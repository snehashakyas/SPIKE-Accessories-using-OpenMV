import hub
import time
hub.port.C.mode(hub.port.MODE_FULL_DUPLEX)
hub.port.C.baud(9600)

while True:
    # Entered LAB values below by user.
    L_val = "3"
    A_val = "-5"
    B_val = "0"
    
    inputVariable = L_val + " " + A_val + " " + B_val
    
    hub.port.C.write(inputVariable)
    time.sleep(1)
    
    a = hub.port.C.read(10)
    print(a) # Prints out if color indicated by user's LAB values have been detected.
    
    time.sleep(1)
