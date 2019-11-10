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
from behaviors.follow_line_behavior import FollowLineBehavior
from behaviors.turn_to_angle_behavior import TurnToAngleBehavior

# Write your program here
bot = SandwichBot()

turn_to = TurnToAngleBehavior(bot, bot.gyro_sensor)
turn_to.run(360)

# while True:
#     print("Angle: ", bot.gyro_sensor.angle())
#     wait(500)

# follow_line = FollowLineBehavior(bot, bot.color_sensor)
# follow_line.run(lambda: any(brick.buttons()))