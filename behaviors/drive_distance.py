from pybricks.ev3devices import GyroSensor, Motor
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from simple_pid import PID

class DriveDistanceBehavior:

    def __init__(self, bot:DriveBase, motor:Motor):
        self.bot = bot
        self.motor = motor
        super().__init__()

    def run(self, distance:int, speed:int):
        self.motor.reset_angle(0)

        while self.motor.angle() < distance:
            self.bot.drive(200, 0)