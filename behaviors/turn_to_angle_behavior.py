from pybricks.ev3devices import GyroSensor
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from simple_pid import PID

class TurnToAngleBehavior:
    PROPORTIONAL = 1.0
    INTEGRAL = -0.0
    DERIVATIVE = 0.0
    UPDATE_INTERVAL = 0.01

    def __init__(self, bot:DriveBase, gyro_sensor:GyroSensor):
        self.bot = bot
        self.gyro_sensor = gyro_sensor
        self.pid = PID(TurnToAngleBehavior.PROPORTIONAL, 
                       TurnToAngleBehavior.INTEGRAL, 
                       TurnToAngleBehavior.DERIVATIVE, 
                       0, 
                       TurnToAngleBehavior.UPDATE_INTERVAL)
        self.__configure_pid()
        super().__init__()

    def __configure_pid(self):
        self.pid.output_limits = (-45, 45)

    def run(self, angle):
        stop_watch = StopWatch()
        self.pid.setpoint = angle
        last_angle = angle + 100
        last_rotation = 0

        while not abs(self.pid.setpoint - last_angle) < 0.25:
            angle = self.gyro_sensor.angle()
            rotation = self.pid(angle)
            if last_rotation != rotation:
                self.bot.drive(0, rotation)
                last_angle = angle
                last_rotation = rotation
                print(stop_watch.time(), ' -- angle:', angle, ', rotation: ', rotation, ', error: ', (angle-self.pid.setpoint))
