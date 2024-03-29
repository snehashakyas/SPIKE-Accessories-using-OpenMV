# SPIKE Accessories using OpenMV

This project adds additional accessories to the *LEGO Education SPIKE Prime* robotics set using the *OpenMV Cam*. The OpenMV Cam is a camera with a microcontroller that can be coded in Python. In this research project, the OpenMV Cam is programmed with the LEGO Foundation's SPIKE Prime, which is a LEGO set for robotics education. This research project will allow the SPIKE Prime robotics set to have the following additional 3 accessories:

1. Color sensors (two different modes).
2. Face detector.
3. Menu Options with both Color Sensor and Face Detector. 

--------

The code in this GitHub project is specific to the following Integrated Development Environments (IDEs):

1. OpenMV IDE for the OpenMV code.
2. Professor Chris Rogers' ME35 "PyView IDE", Version 0.1b06, Tufts University

For all accessories, the user needs to:

1. Upload an appropriate OpenMV script on the OpenMV Cam so that the code runs automatically when connected. To save the script on the OpenMV, open the IDE code and press: Tools > Save open script to OpenMV Cam, and then Tools > Reset OpenMV Cam. The appropriate OpenMV script is specified in the accessory-specific instructions.
2. Connect the SPIKE Prime to a computer and run a script or write code on the *REPL* tab to interact with the SPIKE Prime.
3. Then connect the OpenMV to the computer and SPIKE Prime, as specified on the accessory-specific instructions.

--------

Accessorry-specific Instructions:
------------
The instructions on how to set up and use the color sensor, face detector, and both sensors together are explained below.

Color Sensor
------------

The OpenMV Cam detects a solid block color placed fully enclosed by the OpenMV camera. It then sends the data to a LEGO SPIKE Prime. There are 2 modes for the color sensor.

---------- MODE #1 ----------

Color detection as the OpenMV camera is being moved around its surroundings. SPIKE Prime updates the user with a new detected color each time a color has been detected. 

1. (Needed to have uploaded "ColorSensor Mode1 OPENMV.py" on your OpenMV.)
2. Connect the SPIKE Prime to your computer using a microUSB cable and open "ColorSensor Mode1 SPIKE.py" to run on your SPIKE Prime.
3. Run the code on the SPIKE Prime.
4. Connect your OpenMV to your computer using a microUSB cable.
5. Connect the OpenMV to the SPIKE Prime in Port C of the SPIKE Prime using the white wire coming out of the OpenMV.
6. Move the OpenMV camera around to detect colors. The colors detected will show up on the SPIKE Prime.

More colors to detect can be manually added using the instructions on the comment sections of the "ColorSensor Mode1 OPENMV.py" code.

---------- MODE #2 ----------

User picks a set of LAB color values they would like to sense, and SPIKE PRIME notifies the user when they have scanned the wanted color. 

1. (Needed to have uploaded "ColorSensor Mode2 OPENMV.py" on your OpenMV.)
2. Connect the SPIKE Prime to your computer using a microUSB cable and open "ColorSensor Mode2 SPIKE.py" to run on your SPIKE Prime. Input specific LAB color values you want to detect in the location indicated in the code.
3. Run the code on the SPIKE Prime.
4. Connect your OpenMV to your computer using a microUSB cable.
5. Connect the OpenMV to the SPIKE Prime in Port C of the SPIKE Prime using the white wire coming out of the OpenMV.
6. Move the OpenMV camera around to detect the specified LAB values. The code will run until the LAB values have been detected and you are notified through SPIKE.

Face Detector
--------------- 

The OpenMV detects a face and informs SPIKE Prime once a face has been detected.

1. (Needed to have uploaded "FaceDetector OPENMV.py" on your OpenMV.)
2. Connect the SPIKE Prime to your computer using a microUSB cable and open "ColorSensor Mode1 SPIKE.py" to run on your SPIKE Prime.
3. Run the code on the SPIKE Prime.
4. Connect your OpenMV to your computer using a microUSB cable.
5. Connect the OpenMV to the SPIKE Prime in Port C of the SPIKE Prime using the white wire coming out of the OpenMV.
6. Move the OpenMV camera around to detect a face. The code will run until a face has been detected and you are notified through SPIKE. 

Menu Options with both Color Sensor and Face Detector.
----------------

The user identifies which mode they would like to perform: Color Sensor or Face Detector. The appropriate sensor then runs.

1. (Needed to have uploaded "Combined OPENMV.py" on your OpenMV.)
2. Connect the SPIKE Prime to your computer using a microUSB cable and open "Combined SPIKE.py" to run on your SPIKE Prime.
3. Upload the code on your SPIKE Prime with the name "openmv.py", then run the code on the SPIKE Prime.
4. Type the following on the REPL:

       import openmv
       <variable_name> = openmv.OPENMV(hub.port.<port_letter>, <baud_rate>)
       while(True):
           <variable_name>.readColors() # or <variable_name>.readFaceRecog() if you want to run Face Detector instead of Color Sensor
           
5. Connect your OpenMV to your computer using a microUSB cable.
6. Connect the OpenMV to the SPIKE Prime in any port of the SPIKE Prime using the white wire coming out of the OpenMV. (The user will have specified which port they use in step 4.)
7. Move the OpenMV camera around to detect colors, or to detect a face. For Color Sensor: colors detected will show up on the SPIKE Prime. For Face Detector: the code will run until a face has been detected and you are notified through SPIKE. 
