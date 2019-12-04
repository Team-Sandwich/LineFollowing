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
    def __init__(self, left_motor=Motor(Port.A),
                    right_motor=Motor(Port.B),
                    attachment_motor=(Motor(Port.C)),
                    #wheel_diameter=56, axle_track=110):
                    wheel_diameter=43, axle_track=110):
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.attachment_motor = attachment_motor
        self.color_sensor = ColorSensor(Port.S2)
        self.gyro_sensor = GyroSensor(Port.S1)
        super().__init__(left_motor, right_motor, wheel_diameter, axle_track)

    def follow_line(self, until):
        """
        Follow black line until a condition is met.

        ----------
        angle : float – angle to turn (clockwise - positive).
        """
        follow_line = FollowLineBehavior(self, self.color_sensor)
        follow_line.run(until)

    def turn_to(self, angle):
        """
        Turn the robot for a given angle.

        ----------
        angle : float – angle to turn (clockwise - positive).
        """
        turn_to = TurnToAngleBehavior(self, self.gyro_sensor)
        turn_to.run(angle)

    def drive_distance(self, distance, speed):
        """
        Drive straight using both motors for a given distance and speed.

        ----------
        distance : float – distance measured using motor watch value.

        speed : float – Forward speed of the robot (mm/s).
        """
        drive_distance = DriveDistanceBehavior(self, self.left_motor)
        drive_distance.run(distance, speed)
        self.stop()