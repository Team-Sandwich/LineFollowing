#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

from sandwichbot import SandwichBot

# Write your program here
bot = SandwichBot()

max_reflection = 0
min_reflection = 100
bot.left_motor.reset_angle(0)
stop_watch = StopWatch()

while stop_watch.time() < 2000:
    reflection = bot.color_sensor.reflection()
    if reflection > max_reflection:
        max_reflection = reflection
    if reflection < min_reflection:
        min_reflection = reflection
    bot.drive(100, 0)
    print('reflection:', reflection, ', max_reflection: ', max_reflection, ', min_reflection: ', min_reflection)