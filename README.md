# SPIKE Accessories using OpenMV

1. Color sensors (two different modes).
2. Face detector.

Color Sensor
------------

The OpenMV detects the solid block color placed fully enclosed by the OpenMV camera. It then sends the data to a LEGO SPIKE Prime.

---------- MODE #1 ----------

Color detection as the OpenMV camera is being moved around its surroundings. SPIKE Prime updates the user with a new detected color each time a color has been detected. 

1. Connect the SPIKE Prime to your computer using a microUSB cable and open "ColorSensor Mode1 SPIKE.py" to run on your SPIKE Prime.
2. Connect your OpenMV to your computer using a microUSB cable and open "ColorSensor Mode1 OPENMV.py" to run on your OpenMV IDE.
3. Connect the OpenMV to the SPIKE Prime in Port C of the SPIKE Prime using the white wire coming out of the OpenMV.
4. Run the code on the SPIKE Prime and OpenMV simultaneously.
5. Move the OpenMV camera around to detect colors. The colors detected will show up on the SPIKE Prime.

---------- MODE #2 ----------

User picks a set of LAB color values they would like to sense, and SPIKE pRIME notifies the user when they have scanned the wanted color. 

1. Connect the SPIKE Prime to your computer using a microUSB cable and open "ColorSensor Mode2 SPIKE.py" to run on your SPIKE Prime. Input specific LAB values you want to detect in the location indicated in the code.
2. Connect your OpenMV to your computer using a microUSB cable and open "ColorSensor Mode2 OPENMV.py" to run on your OpenMV IDE.
3. Connect the OpenMV to the SPIKE Prime in Port C of the SPIKE Prime using the white wire coming out of the OpenMV.
4. Run the code on the SPIKE Prime and OpenMV simultaneously.
6. Move the OpenMV camera around to detect the specified LAB values. The code will run until the LAB values have been detected and you are notified through SPIKE.

Face Detector
--------------- 

The OpenMV detects a face, and informs SPIKE Prime once a face has been detected.

1. Connect the SPIKE Prime to your computer using a microUSB cable and open "ColorSensor Mode1 SPIKE.py" to run on your SPIKE Prime.
2. Connect your OpenMV to your computer using a microUSB cable and open "FaceDetector OPENMV.py" to run on your OpenMV IDE.
3. Connect the OpenMV to the SPIKE Prime in Port C of the SPIKE Prime using the white wire coming out of the OpenMV.
4. Run the code on the SPIKE Prime and OpenMV simultaneously.
5. Move the OpenMV camera around to detect a face. The code will run until a face has been detected and you are notified through SPIKE. 
