#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.parameters import (Button)
from pybricks.tools import print, wait, StopWatch

from sandwichbot import SandwichBot
from missions.build_mission import BuildMission
from missions.crane_mission import CraneMission
from missions.ramp_mission import RampMission
from missions.swing_mission import SwingMission

# Write your program here
bot = SandwichBot()

# Clear the display
brick.display.clear()

missions = [SwingMission, BuildMission, CraneMission, RampMission]
selected_mission_index = 0
current_mission_index = 0
brick.display.clear()
brick.display.image(missions[0].IMAGE_PATH)

button_down_active = False
button_up_active = False
button_center_active = False

while True:
    valid_index = selected_mission_index % len(missions)
    if valid_index != current_mission_index:
        selected_mission = missions[valid_index]
        brick.display.clear()
        brick.display.image(selected_mission.IMAGE_PATH)
        current_mission_index = valid_index

    if Button.DOWN in brick.buttons():
        button_down_active = True
    if button_down_active == True and Button.DOWN not in brick.buttons():
        selected_mission_index -= 1
        button_down_active = False
    if Button.UP in brick.buttons():
        button_up_active = True
    if button_up_active == True and Button.UP not in brick.buttons():
        selected_mission_index += 1
        button_up_active = False
    if Button.CENTER in brick. buttons():
        button_center_active =  True
    if button_center_active== True and Button.CENTER not in brick.buttons():
        mission = missions[valid_index](bot)
        mission.run()
        button_center_active = False
