#!/usr/bin/env python3
#The line above must be the first line in the file so the script can be run from Brickman

from ev3dev.ev3 import *
from time import sleep


# GLOBAL VARIABLES FOR MY ROBOT
lcd = Screen()                   # The EV3 display
rightMotor = LargeMotor('outA')  # The motor connected to the right wheel
leftMotor = LargeMotor('outD')   # The motor connected to the left wheel
button = Button()



# USEFUL 'UTILITY' FUNCTIONS FOR MOVEMENT


# Start the motor moving straight at a desired speed (forward if speed is positive and backwards
# if speed is negative), provided the speeds are within safe limits
def startDrivingStraight(desiredSpeed):
  #1000 is the maximum speed the robot can drive at and
  #-1000 is the minimum speed so this checks the value
  #entered meets those conditions.
  if (desiredSpeed <= 1000 and desiredSpeed >= -1000):
    leftMotor.run_forever(speed_sp=desiredSpeed)
    rightMotor.run_forever(speed_sp=desiredSpeed)
  else:
    giveError("Trying to drive too fast")
    sleep(5)

def startTurning(leftSpeed, rightSpeed):
  if (leftSpeed <= 1000 and leftSpeed >= -1000 and 
      rightSpeed<= 1000 and rightSpeed >= -1000):
    leftMotor.run_forever(speed_sp=leftSpeed)
    rightMotor.run_forever(speed_sp=rightSpeed)
  else:
    giveError("Trying to turn too fast")
    sleep(5)
    
def coastToStopDriving():
  rightMotor.stop(stop_action='coast')
  leftMotor.stop(stop_action='coast')
  
def brakeToStopDriving():
  rightMotor.stop(stop_action='brake')
  leftMotor.stop(stop_action='brake')

def holdToStopDriving():
  rightMotor.stop(stop_action='hold')
  leftMotor.stop(stop_action='hold')
 
  
# Test script
if __name__ == '__main__':
  print("Starting testing")
  testMovement()
  print("Done with testing")
  
