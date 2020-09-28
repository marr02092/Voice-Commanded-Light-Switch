# Voice-Commanded-Light-Switch
This is the project I submitted to College Board as my final for AP Computer Science principles and got a 5/5.

I came up with the idea of this project because many times I found myself not wanting to stand up and walk to the light switch to turn it on or off, so I made this wireless switch operator, it can be used through voice commands or with a remote control.


This project consists of three parts:
  
  
  -The python script running in the pc, which through voice recognition listens for a voice command and when it is received it will communicate with the IR Sender.
  
  
  -IR Sender is an Arduino Uno which has an Infra Red LED, it is connected through usb to the pc and is listening for a message throug serial port from the python script, 
  when it receives the message it will send an IR signal to the IR receiver and switch actuator.
  
  
  
  -An Arduino Nano is attached to the wall close to the light switch, it has an IR receiver, when receives the signal it triggers a stepper motor which actuates the light switch.
  
  VIEW DIAGRAM AND CODE FOR FURTHER UNDERSTANDING!!  :D
