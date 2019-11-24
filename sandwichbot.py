from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, ColorSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

from behaviors.follow_line_behavior import FollowLineBehavior
from behaviors.turn_to_angle_behavior import TurnToAngleBehavior
from behaviors.drive_distance import DriveDistanceBehavior

class SandwichBot(DriveBase):
    def __init__(self, left_motor=Motor(Port.A), right_motor=Motor(Port.B), wheel_diameter=56, axle_track=110):
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.color_sensor = ColorSensor(Port.S2)
        self.gyro_sensor = GyroSensor(Port.S1)
        super().__init__(left_motor, right_motor, wheel_diameter, axle_track)

    def follow_line(self, until):
        follow_line = FollowLineBehavior(self, self.color_sensor)
        follow_line.run(until)

    def turn_to(self, angle):
        turn_to = TurnToAngleBehavior(self, self.gyro_sensor)
        turn_to.run(angle)

    def drive_distance(self, distance, speed):
        drive_distance = DriveDistanceBehavior(self, self.left_motor)
        drive_distance.run(distance, speed)