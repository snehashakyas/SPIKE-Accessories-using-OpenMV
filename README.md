# SPIKE Accessories using OpenMV

1. Color sensors (two different modes).
2. Face detector.
3. Menu Options with both Color Sensor and Face Detector.

For all accessories, the user needs to:

1. Upload the appropriate OpenMV script on it so that the OpenMV code runs automatically when connected. To save the script on the OpenMV, open the IDE code and press: Tools > Save open script to OpenMV Cam, and then Tools > Reset OpenMV Cam. The appropriate OpenMV script is specified in the accessory-specific instructions below.
2. Connect the SPIKE Prime to their computer and run a script or write code on the REPL to interact with the SPIKE Prime.
3. Then connect the OpenMV to the computer and SPIKE, as specified on the accessory-specific instructions below.

Color Sensor
------------

The OpenMV detects the solid block color placed fully enclosed by the OpenMV camera. It then sends the data to a LEGO SPIKE Prime.

---------- MODE #1 ----------

Color detection as the OpenMV camera is being moved around its surroundings. SPIKE Prime updates the user with a new detected color each time a color has been detected. 

1. (Needed to have uploaded "ColorSensor Mode1 OPENMV.py" on your OpenMV.)
2. Connect the SPIKE Prime to your computer using a microUSB cable and open "ColorSensor Mode1 SPIKE.py" to run on your SPIKE Prime.
3. Connect your OpenMV to your computer using a microUSB cable.
4. Connect the OpenMV to the SPIKE Prime in Port C of the SPIKE Prime using the white wire coming out of the OpenMV.
5. Run the code on the SPIKE Prime.
6. Move the OpenMV camera around to detect colors. The colors detected will show up on the SPIKE Prime.

---------- MODE #2 ----------

User picks a set of LAB color values they would like to sense, and SPIKE pRIME notifies the user when they have scanned the wanted color. 

1. (Needed to have uploaded "ColorSensor Mode2 OPENMV.py" on your OpenMV.)
2. Connect the SPIKE Prime to your computer using a microUSB cable and open "ColorSensor Mode2 SPIKE.py" to run on your SPIKE Prime. Input specific LAB values you want to detect in the location indicated in the code.
3. Connect your OpenMV to your computer using a microUSB cable.
4. Connect the OpenMV to the SPIKE Prime in Port C of the SPIKE Prime using the white wire coming out of the OpenMV.
5. Run the code on the SPIKE Prime.
6. Move the OpenMV camera around to detect the specified LAB values. The code will run until the LAB values have been detected and you are notified through SPIKE.

Face Detector
--------------- 

The OpenMV detects a face, and informs SPIKE Prime once a face has been detected.

1. (Needed to have uploaded "FaceDetector OPENMV.py" on your OpenMV.)
2. Connect the SPIKE Prime to your computer using a microUSB cable and open "ColorSensor Mode1 SPIKE.py" to run on your SPIKE Prime.
3. Connect your OpenMV to your computer using a microUSB cable.
4. Connect the OpenMV to the SPIKE Prime in Port C of the SPIKE Prime using the white wire coming out of the OpenMV.
5. Run the code on the SPIKE Prime.
6. Move the OpenMV camera around to detect a face. The code will run until a face has been detected and you are notified through SPIKE. 

Menu Options with both Color Sensor and Face Detector.
----------------

The user identifies which mode they would like to perform: Color Sensor or Face Detector. The appropriate code then runs.

1. (Needed to have uploaded "Combined OPENMV.py" on your OpenMV.)
2. Connect the SPIKE Prime to your computer using a microUSB cable and open "Combined SPIKE.py" to run on your SPIKE Prime.
3. Connect your OpenMV to your computer using a microUSB cable.
4. Connect the OpenMV to the SPIKE Prime in any port of the SPIKE Prime using the white wire coming out of the OpenMV. (The user will need to specify which port they use later.)
5. Run the code on the SPIKE Prime.
6. Type the following on the REPL:

       import openmv
       <variable_name> = openmv.OPENMV(hub.port.<port_letter>, <baud_rate>)
       while(True):
           <variable_name>.readColors() # or <variable_name>.readFaceRecog() if you want to run Face Detector instead of Color Sensor
           
    
7. Move the OpenMV camera around to detect colors, or to detect a face. 
   For Color Sensor: colors detected will show up on the SPIKE Prime
   For Face Detector: the code will run until a face has been detected and you are notified through SPIKE. 
