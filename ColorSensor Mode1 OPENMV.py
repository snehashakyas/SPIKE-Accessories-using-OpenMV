# Color Sensor that Sends a Color Name to SPIKE Prime continuosly.
# May 27 2021, Sneha Shakya

# This code currently allows detection of 3 colors: red, black, and yellow. 
# More colors to detect can be manually added by determining appropriate color
#     thresholds and adding them in the if-statements below.

from pyb import UART
import sensor, image, time
uart = UART(3, 9600, timeout_char=1000)
uart.init(9600, bits=8, parity=None, stop=1, timeout_char=1000)

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False)
sensor.set_auto_whitebal(False)
clock = time.clock()

color = "Undetected"

# Capturing color thresholds center of the image.
r = [(320//2)-(50//2), (240//2)-(50//2), 10, 10]

# Color Tracking: 
    # thresholds[L Min, L Max, A Min, A Max, B Min, B Max]
    # L - lightness
    # A - red/green value
    # B - blue/yellow value

    # Generic thresholds:
    # thresholds = (30, 100, 15, 127, 15, 127) = red
                 # (1, 49, -14, 9, -11, 22) = black
                 # (40, 79, -21, 5, -18, 67) = yellow
                 # Can add more color thresholds here.

print(" ")
print("Hold OpenMV infront of objects to detect their color.")

for i in range(60):
    img = sensor.snapshot()
    img.draw_rectangle(r)

threshold = [50, 50, 0, 0, 0, 0] # Middle L, A, B values to inilialize.

while True:
    img = sensor.snapshot()
    hist = img.get_histogram(roi=r)
    lo = hist.get_percentile(0.01)
    hi = hist.get_percentile(0.99)

    # Average in percentile values.
    threshold[0] = (threshold[0] + lo.l_value()) // 2
    threshold[1] = (threshold[1] + hi.l_value()) // 2
    threshold[2] = (threshold[2] + lo.a_value()) // 2
    threshold[3] = (threshold[3] + hi.a_value()) // 2
    threshold[4] = (threshold[4] + lo.b_value()) // 2
    threshold[5] = (threshold[5] + hi.b_value()) // 2

    for blob in img.find_blobs([threshold], pixels_threshold=100, area_threshold=100, merge=True,
    margin=10):
        img.draw_rectangle(blob.rect())
        img.draw_cross(blob.cx(), blob.cy())
        img.draw_rectangle(r)

    clock.tick()
    img = sensor.snapshot()
    for blob in img.find_blobs([threshold], pixels_threshold=100, area_threshold=100, merge=True,
    margin=10):
        img.draw_rectangle(blob.rect())
        img.draw_cross(blob.cx(), blob.cy())

    if (threshold[0] >= 30 and threshold[1] <= 100 and threshold[2] >= 15 and threshold[3] <= 127
    and threshold[4] >= 15 and threshold[5] <= 127):
        color = "red"
        print(color)
        uart.write(color)
        time.sleep(1)

    if (threshold[0] >= 1 and threshold[1] <= 49 and threshold[2] >= -14 and threshold[3] <= 9
    and threshold[4] >= -11 and threshold[5] <= 22):
        color = "black"
        print(color)
        uart.write(color)
        time.sleep(1)

    if (threshold[0] >= 40 and threshold[1] <= 79 and threshold[2] >= -21 and threshold[3] <= 5
    and threshold[4] >= -18 and threshold[5] <= 67):
        color = "yellow"
        print(color)
        uart.write(color)
        time.sleep(1)
    
    # Add more colors to detect using the template below:
    
    # if (threshold[0] >= <L Min> and threshold[1] <= <L Max> and threshold[2] >= <A Min> 
    # and threshold[3] <= <A Max> and threshold[4] >= <B Min> and threshold[5] <= <B Max>):
        # color = "<added color>"
        # print(color)
        # uart.write(color)
        # time.sleep(1)
