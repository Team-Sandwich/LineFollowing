#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.parameters import (Button, Stop)
from pybricks.tools import print, wait, StopWatch

from sandwichbot import SandwichBot
from missions.build_mission import BuildMission
from missions.build2_mission import Build2Mission
from missions.traffic_mission import TrafficMission

# set up robot
bot = SandwichBot()

# Clear the display
brick.display.clear()

#Setting up the user interface
missions = [TrafficMission, BuildMission, Build2Mission]
selected_mission_index = 0
current_mission_index = 0
brick.display.clear()
brick.display.image(missions[0].IMAGE_PATH)

last_buttons_pressed = set()

while True:
    buttons_released = last_buttons_pressed - set(brick.buttons())
    last_buttons_pressed = set(brick.buttons())

    if last_buttons_pressed:
        if Button.LEFT in last_buttons_pressed:
            bot.attachment_motor.run(-360)

        if Button.RIGHT in last_buttons_pressed:
            bot.attachment_motor.run(360)

    if buttons_released:
        if Button.DOWN in buttons_released:
            selected_mission_index -= 1

        if Button.UP in buttons_released:
            selected_mission_index += 1

        valid_index = selected_mission_index % len(missions)
        if valid_index != current_mission_index:
            selected_mission = missions[valid_index]
            brick.display.clear()
            brick.display.image(selected_mission.IMAGE_PATH)
            current_mission_index = valid_index

        if Button.CENTER in buttons_released:
            mission = missions[valid_index](bot)
            mission.run()

        if Button.LEFT in buttons_released:
            bot.attachment_motor.stop()

        if Button.RIGHT in buttons_released:
            bot.attachment_motor.stop()
    else:
        wait(10)
