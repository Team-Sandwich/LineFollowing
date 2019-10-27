from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

class SandwichBot(DriveBase):
    def __init__(self, left_motor=Motor(Port.A), right_motor=Motor(Port.B), wheel_diameter=56, axle_track=114):
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.color_sensor = ColorSensor(Port.S2)
        super().__init__(left_motor, right_motor, wheel_diameter, axle_track)
