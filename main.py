#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from simple_pid import PID

from sandwichbot import SandwichBot

# Write your program here
bot = SandwichBot()

max_reflection = 77
min_reflection = 4
target_reflection = (max_reflection - min_reflection) / 2
stop_watch = StopWatch()
pid = PID(-5.0, -2.5, 0, target_reflection, 0.01)
pid.output_limits = (-45, 45)
last_angle = 0

while not any(brick.buttons()):
    reflection = bot.color_sensor.reflection()
    angle = pid(reflection)
    if angle != last_angle:
        bot.drive(50, angle)
        print(stop_watch.time(), ' -- reflection:', reflection, ', angle: ', angle, ', error: ', (reflection-target_reflection))
        last_angle = angle
