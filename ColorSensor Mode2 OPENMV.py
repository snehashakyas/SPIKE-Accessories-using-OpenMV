# Allows the user to pick their own LAB values on SPIKE and use the OpenMV to detect them in their
#                                                                                    surroundings.
# March 31 2021, Sneha Shakya

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

done = True

while(done):
    input = uart.readline()
    stringInput = str(input)
    length = len(stringInput)
    length = length - 3

    concatenatedInput = stringInput[2:2+length]
    array = concatenatedInput.split(' ')

    L_Value = array[0]

    try:
        A_Value = array[1]
        B_Value = array[-1]
        done = False
    except:
      print("Length of array is updateing. It is currently " + str(len(array)))


print(L_Value, " ", A_Value, " ", B_Value)

# Adding a range to the user's LAB values because external factors can affect color of detected LAB
LMin = int(L_Value) - 5
LMax = int(L_Value) + 5
AMin = int(A_Value) - 5
AMax = int(A_Value) + 5
BMin = int(B_Value) - 5
BMax = int(B_Value) + 5

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
        uart.write("Detected")
