# Returns true to user if a face is detected.

from pyb import UART
import sensor, image, pyb, time
uart = UART(3, 9600, timeout_char=1000)
uart.init(9600, bits=8, parity=None, stop=1, timeout_char=1000)

RED_LED_PIN = 1
BLUE_LED_PIN = 3

sensor.reset() # Initialize the camera sensor.
sensor.set_pixformat(sensor.GRAYSCALE)
sensor.set_framesize(sensor.HQVGA) # or sensor.QQVGA (or others)
sensor.skip_frames(time = 2000) # Let new settings take affect.

face_cascade = image.HaarCascade("frontalface", stages=25)

while(True):
    found = False
    pyb.LED(RED_LED_PIN).on()
    print("About to start detecting faces...")
    sensor.skip_frames(time = 2000) # Give the user time to get ready.

    pyb.LED(RED_LED_PIN).off()
    print("Now detecting faces!")
    pyb.LED(BLUE_LED_PIN).on()

    diff = 10 # detect a face after 10 frames.
    while(diff):
        img = sensor.snapshot()

        faces = img.find_features(face_cascade, threshold=0.5, scale_factor=1.5)

        if faces:
            diff -= 1
            for r in faces:
                img.draw_rectangle(r)

    found = True

    if (found == True):
        pyb.LED(BLUE_LED_PIN).off()
        print("Face detected! Informing SPIKE...")
        print(found)
        uart.write("Detected!")

    time.sleep(1000)

