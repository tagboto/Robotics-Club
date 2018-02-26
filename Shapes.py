#!/usr/bin/env python3

import movement_library as m

# To make the robot draw a square with sides of length 30 cm
def square(speed, distance):
  for i in range(4):
    m.moveForward(500, 30)
    m.turnLeft(200)
    
    
