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

# Clear the display
brick.display.clear()

time = StopWatch()

missions = ['build.jpg', 'swing.jpg', 'ramp.jpg', 'crane.jpg']
selected_mission_index = 0
current_mission_index = 0
brick.display.clear()
brick.display.image("assets/" + missions[0])

button_down_active = False
button_up_active = False
button_center_active = False

while True:
    valid_index = selected_mission_index % len(missions)
    if valid_index != current_mission_index:
        selected_mission = missions[valid_index]
        print("valid_index: ", valid_index, "selected_mission_index", selected_mission_index)
        brick.display.clear()
        brick.display.image("assets/" + selected_mission)
        current_mission_index = valid_index

    if Button.DOWN in brick.buttons():
        button_down_active = True
    if button_down_active == True and Button.DOWN not in brick.buttons():
        selected_mission_index -= 1
        button_down_active = False
        print("DN")
    if Button.UP in brick.buttons():
        button_up_active = True
    if button_up_active == True and Button.UP not in brick.buttons():
        print("UP")
        selected_mission_index += 1
        button_up_active = False
    if Button.CENTER in brick. buttons():
        button_center_active =  True
    if button_center_active== True and Button.CENTER not in brick.buttons():
        print("CENTER")
        button_center_active = False

# time.time() < 5000:
    # wait(100)




# turn_to = TurnToAngleBehavior(bot, bot.gyro_sensor)
# turn_to.run(360)

# while True:
#     print("Angle: ", bot.gyro_sensor.angle())
#     wait(500)

# follow_line = FollowLineBehavior(bot, bot.color_sensor)
# follow_line.run(lambda: any(brick.buttons()))