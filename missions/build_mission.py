from pybricks import ev3brick as brick
from pybricks.tools import print, wait, StopWatch
from sandwichbot import SandwichBot

class BuildMission():
    IMAGE_PATH = "assets/build.jpg"

    def __init__(self, bot:SandwichBot):
        self.image_path = BuildMission.IMAGE_PATH
        self.bot = bot

    def run(self):
        brick.sound.beep()
        print("Run Build Mission")
        turn_to = TurnToAngleBehavior(bot, bot.gyro_sensor)
        turn_to.run(-11)

        target_distance = 1237
        bot.left_motor.reset_angle(0)

        while bot.left_motor.angle() < target_distance:
            self.bot.drive(150, 0)

        while bot.left_motor.angle() > -340:
            self.bot.drive(-500, 0)
