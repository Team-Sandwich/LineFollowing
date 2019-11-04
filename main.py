#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, ColorSensor)
from pybricks.parameters import (Port, Stop, Direction, Color)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

def measure_values(drive_base, color_sensor):
    # Calibrate min and max reflection values
    reflection_max = 0
    reflection_min = 100
    run_timer = StopWatch()
    run_timer.reset()

    while run_timer.time() < 3000:
        reflection = color_sensor.reflection()
        if reflection_max < reflection:
            reflection_max = reflection
        if reflection_min > reflection:
            reflection_min = reflection
        robot_sandwich_bob.drive(200, 0)

    print("reflection_max: ", reflection_max, ", reflection_min: ", reflection_min)

def follow_line(drive_base, color_sensor):
    lastError = error = integral = 0
    reflection_min = 4  # on black
    reflection_max = 91 # on white
    # target = (reflection_max + reflection_min) / 2
    target = 20
    kp = float(0.85)
    kd = 1
    ki = float(0.03)
    direction = 1
    speed_mm_per_sec = 60
    duration_in_ms = 60

    while True:
        reflection = color_sensor.reflection()
        # brick.display.text("Reflection: {}".format(reflection))
        # wait(200)
        error = target - (100 * ( reflection - reflection_min ) / ( reflection_max - reflection_min ))
        derivative = error - lastError
        lastError = error
        integral = float(0.5) * integral + error
        steering = (kp * error + kd * derivative + ki * integral) * direction
        # print("steering: ", steering, ", error: ", error)
        brick.display.text("s: {:.1f}, e: {:.1f}".format(steering, error))
        robot_sandwich_bob.drive_time(speed_mm_per_sec, steering, duration_in_ms) # 10Hz

# settings for XRay robot
motor_a = Motor(Port.A)
motor_b = Motor(Port.B)
wheelDia_in_mm = 40
axleWidth_in_mm = 112
color_sensor = ColorSensor(Port.S1)

robot_sandwich_bob = DriveBase(motor_a, motor_b, wheelDia_in_mm, axleWidth_in_mm)

# brick.sound.beep()
brick.display.clear()

# measure_values(robot_sandwich_bob, color_sensor)
follow_line(robot_sandwich_bob, color_sensor)
