# Hand_Tracking_Servo_Turner_with_Arduino
This uses python and c++ to move a servo connected to an arduino with hand movements

WIRING:

  Components:
    Servo (3 pin slots)
    Arduino (uno, nano, etc)
  Wiring:
    Servo Red to 5V
    Servo Brown to GND
    Servo Yellow to Digital Pin 9
    

HOW TO USE:

1. Go to Arduino IDE and click on file=>examples=>Firmata=>StandardFirmata
2. Once the Arduino Editor Firmata is open, copy paste the code into the editor and upload it. (Make Sure WIRING is set)
3. Next open a python file
4. Instal modules needed  "pip install opencv-python
                           pip install mediapipe
                           pip install pyserial"
   
6. Paste the python code provided (default mac, but uncomment windows port if needed)
5. Run Code and See Results
