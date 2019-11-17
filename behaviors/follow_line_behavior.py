from pybricks.ev3devices import ColorSensor
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from simple_pid import PID

class FollowLineBehavior:
    PROPORTIONAL = -1.0
    INTEGRAL = -.25
    DERIVATIVE = 0.0
    UPDATE_INTERVAL = 0.01

    def __init__(self, bot:DriveBase, color_sensor:ColorSensor):
        self.bot = bot
        self.color_sensor = color_sensor
        self.max_reflection = 94
        self.min_reflection = 12
        self.pid = PID(FollowLineBehavior.PROPORTIONAL, 
                       FollowLineBehavior.INTEGRAL, 
                       FollowLineBehavior.DERIVATIVE, 
                       0, 
                       FollowLineBehavior.UPDATE_INTERVAL)
        self.__configure_pid()

        super().__init__()

    def __configure_pid(self):
        self.pid.setpoint = (self.max_reflection - self.min_reflection) / 2
        self.pid.output_limits = (-45, 45)
        pass

    def run(self, until):
        stop_watch = StopWatch()
        last_angle = 0

        while not until():
            reflection = self.color_sensor.reflection()
            angle = self.pid(reflection)
            if last_angle != angle:
                self.bot.drive(50, angle)
                last_angle = angle
                print(stop_watch.time(), ' -- reflection:', reflection, ', angle: ', angle, ', error: ', (reflection-self.pid.setpoint))
