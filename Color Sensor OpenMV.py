# Color Sensor that Sends a Color Name to SPIKE Prime.
# March 24 2021, Sneha Shakya

from pyb import UART
import sensor, image, time
uart = UART(3, 9600, timeout_char=1000)
uart.init(9600, bits=8, parity=None, stop=1, timeout_char=1000)

executed = False
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False)
sensor.set_auto_whitebal(False)
clock = time.clock()

# Capturing color thresholds center of the image.
r = [(320//2)-(50//2), (240//2)-(50//2), 10, 10]

# Color Tracking: thresholds[L Min, L Max, A Min, A Max, B Min, B Max]
# L - lightness
# A - red/green value
# B - blue/yellow value

# Generic thresholds:
# thresholds = (30, 100, 15, 127, 15, 127) = red
             # (1, 49, -14, 9, -11, 22) = black
             # (40, 79, -21, 5, -18, 67) = yellow

print(" ")
print("Hold the object of a block color 2cm in front of the camera in the box, fully enclosed!")

for i in range(60):
    img = sensor.snapshot()
    img.draw_rectangle(r)

print("Tracking color thresholds... You have 5 seconds to place the object in the right spot.")
print(" ")
threshold = [50, 50, 0, 0, 0, 0] # Middle L, A, B values to inilialize.

for i in range(60):
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

    # gives user 5 seconds to hold the camera infront of the object for a while, until the values
    #                                                are not read anymore, and the camera pauses.

    threshold_L_min = threshold[0]
    threshold_L_max = threshold[1]
    threshold_A_min = threshold[2]
    threshold_A_max = threshold[3]
    threshold_B_min = threshold[4]
    threshold_B_max = threshold[5]

    # print(threshold_L_min, " ", threshold_L_max, " ", threshold_A_min, " ", threshold_A_max,
    #                                              " ", threshold_B_min, " ", threshold_B_max)

while(executed == False):
    if (threshold[0] >= 30 and threshold[1] <= 100 and threshold[2] >= 15 and threshold[3] <= 127
    and threshold[4] >= 15 and threshold[5] <= 127):
        color = "red"
        uart.write(color)
        time.sleep(1000)
        executed = True

    if (threshold[0] >= 1 and threshold[1] <= 49 and threshold[2] >= -14 and threshold[3] <= 9
    and threshold[4] >= -11 and threshold[5] <= 22):
        color = "black"
        uart.write(color)
        time.sleep(1000)
        executed = True

    if (threshold[0] >= 40 and threshold[1] <= 79 and threshold[2] >= -21 and threshold[3] <= 5
    and threshold[4] >= -18 and threshold[5] <= 67):
        color = "yellow"
        uart.write(color)
        time.sleep(1000)
        executed = True

    if (executed == False):
        color = "Error"
        uart.write(color)
        executed = True

print("Detected color: ", color)

while True:
    uart.write(color)
    time.sleep(1000)
