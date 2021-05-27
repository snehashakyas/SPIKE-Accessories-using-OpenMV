import hub
import time
hub.port.C.mode(hub.port.MODE_FULL_DUPLEX) # OpenMV connected to Port C in SPIKE.
hub.port.C.baud(9600)

a = hub.port.C.read(10) # To discard first read value, which is always '\xff'.

while True:
    # Enter LAB values below, in between the apostrophes. For example, right now the LAB values correspond to 3, -5, and 0 respectively.
    L_val = "-3"
    A_val = "-5"
    B_val = "0"

    inputVariable = L_val + " " + A_val + " " + B_val
    
    # Current bug in code: the below line causes a number to be printed out in the SPIKE, which is unwanted. 
    hub.port.C.write(inputVariable)
    
    a = hub.port.C.read(10)
    if(len(a) != 0):
        print(a) # Prints if LAB values you indicate have been detected.

    time.sleep(1)
