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

        while not self.__at_target(distance, self.motor):
            if distance >= 0:
                self.bot.drive(speed, 0)
            else:
                self.bot.drive(-speed, 0)
            print("Drive Distance -- target: ", distance, ", distance: ", self.motor.angle())

    def __at_target(self, distance:int, motor) -> bool:
        if distance >= 0:
            return self.motor.angle() > distance
        else:
            return self.motor.angle() < distance
