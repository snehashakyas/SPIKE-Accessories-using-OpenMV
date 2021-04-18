# SPIKE Accessories using OpenMV

1. Color sensors (two different modes).
2. Face detector.

---------- COLOR SENSOR -------------------------------------------------------------------------------------------------------

The OpenMV detects the solid block color placed fully enclosed by the OpenMV camera. It then sends the data to a LEGO SPIKE Prime.

Mode #1: Color detection as the OpenMV camera is being moved around its surroundings. SPIKE Prime updates the user with a new detected color each time a color has been detected. 

Using "InfiniteSensing OpenMV.py" in OpenMV IDE:

This code senses 
1. Move the OpenMV camera around to detect colors.

How to use set-up OpenMV Color Sensor codes:
1. Connect your SPIKE Prime to your computer using a microUSB cable and open "Color Sensor SPIKE.py" to run on your SPIKE Prime.
2. Connect your OpenMV to your computer using a microUSB cable and open only one of the OpenMV Color Sensor codes to run on your OpenMV IDE. The OpenMV Color Sensor codes are: "Color Sensor OpenMV.py", "UserPick OpenMV.py", and "InfiniteSensing OpenMV". Below will talk more about how each of these codes differ. 
3. Connect the OpenMV to the SPIKE Prime in Port C of the SPIKE Prime using the white wire coming out of the OpenMV.
4. Run the code on the SPIKE Prime and OpenMV simultaneously.


Using "UserPick OpenMV.py" in OpenMV IDE:

This code allows the user to pick a set of LAB color values they would like to sense, and notifies the user when they have scanned the wanted color. 
1. Move the OpenMV camera around until you are notified that the specified LAB colors have been detected.


