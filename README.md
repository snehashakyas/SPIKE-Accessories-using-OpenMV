# OpenMV-Color-Sensor
Creating a color sensor using OpenMV

The OpenMV detects the color placed in front of it, and sends the data to a LEGO SPIKE Prime.

How to use set-up OpenMV Color Sensor codes:
1. Connect your SPIKE Prime to your computer using a microUSB cable and open "Color Sensor SPIKE.py" to run on your SPIKE Prime.
2. Connect your OpenMV to your computer using a microUSB cable and open only one of the OpenMV Color Sensor codes to run on your OpenMV IDE. The OpenMV Color Sensor codes are: "Color Sensor OpenMV.py", "UserPick OpenMV.py", and "InfiniteSensing OpenMV". Below will talk more about how each of these codes differ. 
3. Connect the OpenMV to the SPIKE Prime in Port C of the SPIKE Prime using the white wire coming out of the OpenMV.
4. Run the code on the SPIKE Prime and OpenMV simultaneously.



Using "Color Sensor OpenMV.py" in OpenMV IDE:
This code senses one color at a time, each time the code is run. Here is how to scan a color.
1. You have 5 seconds to place the OpenMV camera in front of the object to be scanned. 
2. Place the OpenMV camera 2 cm in front of the object to be scanned. 
3. After 5 seconds, the screen will pause and the color detected will be output on the LEGO SPIKE Prime. This data can then be used for SPIKE Prime activities accordingly.


Using "UserPick OpenMV.py" in OpenMV IDE:
This code allows the user to pick a set of LAB color values they would like to sense, and notifies the user when they have scanned the wanted color. 
1. Move the OpenMV camera around until you are notified that the specified LAB colors have been detected.


Using "InfiniteSensing OpenMV.py" in OpenMV IDE:
This code senses colors as the OpenMV camera is being moved around in its surroundings, and updates the user with a new detected color each time a color has been detected. 
1. Move the OpenMV camera around to detect colors.


Note: for all OpenMV codes, the object you are scanning must be a solid block color (e.g. a LEGO brick). Use the OpenMV IDE to make sure that the object you would like to scan is fully enclosed by the OpenMV camera -- only one solid block color should be showing on the screen.



