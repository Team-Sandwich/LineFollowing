from pybricks.ev3devices import ColorSensor, Motor
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from simple_pid import PID

class FollowLineBehavior:
    """
    Behavior class to drive two powered wheels following a line using the color sensor.
    """

    PROPORTIONAL = -0.7
    INTEGRAL = -0.05
    DERIVATIVE = -0.05
    UPDATE_INTERVAL = None

    def __init__(self, bot:DriveBase, color_sensor:ColorSensor, use_left_edge:bool, motor:Motor):
        self.bot = bot
        self.color_sensor = color_sensor
        self.motor = motor
        self.max_reflection = 94
        self.min_reflection = 12

        Kp = FollowLineBehavior.PROPORTIONAL if use_left_edge else -FollowLineBehavior.PROPORTIONAL
        Ki = FollowLineBehavior.INTEGRAL if use_left_edge else -FollowLineBehavior.INTEGRAL
        Kd = FollowLineBehavior.DERIVATIVE if use_left_edge else -FollowLineBehavior.DERIVATIVE
        self.pid = PID(Kp, Ki, Kd, 0, FollowLineBehavior.UPDATE_INTERVAL)
        self.__configure_pid()

        super().__init__()

    def __configure_pid(self):
        self.pid.setpoint = (self.max_reflection - self.min_reflection) / 2
        self.pid.output_limits = (-45, 45)
        pass

    def __at_target(self, distance:int, motor) -> bool:
        if distance >= 0:
            return self.motor.angle() > distance
        else:
            return self.motor.angle() < distance

    def run_distance(self, distance:int):
        """
        Start following a line for the specified distance.

        ----------
        distance : int – distance measured in wheel angular turn degree using motor watch value.
        """
        stop_watch = StopWatch()
        self.motor.reset_angle(0)
        last_angle = 0

        while not self.__at_target(distance, self.motor):
            reflection = self.color_sensor.reflection()
            angle = self.pid(reflection)
            if last_angle != angle:
                self.bot.drive(50, angle)
                last_angle = angle
                print(stop_watch.time(), ' -- reflection:', reflection, ', angle: ', angle, ', error: ', (reflection-self.pid.setpoint))

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
