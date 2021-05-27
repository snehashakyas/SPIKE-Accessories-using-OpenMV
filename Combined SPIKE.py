import hub
import time

class OPENMV:
    def __init__(self, port, baud=9600):
        self.s=port
        self.s.mode(hub.port.MODE_FULL_DUPLEX)
        time.sleep(0.1)
        self.s.baud(9600)
        
    def readColors(self):
        self.s.write('$color')
        time.sleep(0.2)
        a = self.s.read(7)
        if(len(a) != 0):
            print(a)
              
    def readFaceRecog(self):
        self.s.write('$faces')
        time.sleep(0.2)
        b = self.s.read(10)
        if(len(b) != 0):
           print(b)
