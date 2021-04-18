# SPIKE Accessories using OpenMV

1. Color sensors (two different modes).
2. Face detector.

COLOR SENSOR
------------

The OpenMV detects the solid block color placed fully enclosed by the OpenMV camera. It then sends the data to a LEGO SPIKE Prime.

---------- MODE #1 ----------
Color detection as the OpenMV camera is being moved around its surroundings. SPIKE Prime updates the user with a new detected color each time a color has been detected. 

1. Connect the SPIKE Prime to your computer using a microUSB cable and open "Color Sensor SPIKE.py" to run on your SPIKE Prime.
2. Connect your OpenMV to your computer using a microUSB cable and open "InfiniteSensing OpenMV.py" to run on your OpenMV IDE.
3. Connect the OpenMV to the SPIKE Prime in Port C of the SPIKE Prime using the white wire coming out of the OpenMV.
4. Run the code on the SPIKE Prime and OpenMV simultaneously.
5. Move the OpenMV camera around to detect colors. The colors detected will show up on the SPIKE Prime.

---------- MODE #2 ----------
User picks a set of LAB color values they would like to sense, and SPIKE pRIME notifies the user when they have scanned the wanted color. 

Using "UserPick OpenMV.py" in OpenMV IDE:

1. Move the OpenMV camera around until you are notified that the specified LAB colors have been detected.


