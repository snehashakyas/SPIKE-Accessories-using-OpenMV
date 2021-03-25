# Allows the user to pick their own LAB values and use the OpenMV to detect them in their
#                                                                           surroundings.
# March 24 2021, Sneha Shakya

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

sensed = False

# Capturing color thresholds center of the image.
r = [(320//2)-(50//2), (240//2)-(50//2), 10, 10]

print(" ")
# print("Enter the LAB threshold values you are searching for.")
# L_value = uart.read(10)
# A_value = uart.read(10)
# B_value = uart.read(10)

# Cannot find a way to enter values in the terminal as of yet.
# Therefore setting temporary values that the user should be able to manipulate:
L_value = 3
A_value = -5
B_value = 0

# Adding a range to the user's LAB values because external factors can affect color of detected LAB
LMin = L_value - 5
LMax = L_value + 5
AMin = A_value - 5
AMax = A_value + 5
BMin = B_value - 5
BMax = B_value + 5

for i in range(60):
    img = sensor.snapshot()
    img.draw_rectangle(r)

print("Tracking color thresholds... Program will stop when LAB colors are detected.")
print(" ")
threshold = [50, 50, 0, 0, 0, 0] # Middle L, A, B values to inilialize.

while(sensed == False):
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
    print(threshold[0], " ", threshold[1], " ", threshold[2], " ", threshold[3]," ", threshold[4],
    " ", threshold[5])

    if (threshold[0] >= LMin and threshold[1] <= LMax and threshold[2] >= AMin
    and threshold[3] <= AMax and threshold[4] >= BMin and threshold[5] <= BMax):
        sensed = True
        print("Color with specified LAB values detected.")
        uart.write("Color detected")
