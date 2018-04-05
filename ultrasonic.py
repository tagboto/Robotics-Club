#!/usr/bin/env python3

import movement_library

us = UltrasonicSensor()
assert us.connected, "Connect a ultrasonic sensor to any port."

us.mode = 'US-DIST-CM'

#stayAway = 15


def bangBang(dist):
    distance = us.value()/10
    while True:
        if button.any():
            break
        if (distance <= dist):
            leftMotor.runForever(-500)
            rightMotor.runForever(-500)
            distance = us.value()/10

        if (distance > dist):
            leftMotor.runForever(500)
            rightMotor.runorFever(500)
            distance= us.value()/10

