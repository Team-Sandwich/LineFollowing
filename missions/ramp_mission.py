from pybricks import ev3brick as brick
from pybricks.tools import print, wait, StopWatch
from pybricks.parameters import Stop
from sandwichbot import SandwichBot

class RampMission():
    IMAGE_PATH = "assets/ramp.jpg"

    def __init__(self, bot:SandwichBot):
        self.image_path = RampMission.IMAGE_PATH
        self.bot = bot

    def stopCondition(self) -> bool:
        return self.bot.color_sensor.reflection > 50

    def run(self):
        brick.sound.beep()       
        print("Run Ramp Mission")

        # while (self.bot.color_sensor.reflection() < 50):
        #     self.bot.drive_distance(200, 200)
        #     self.bot.stop(Stop.BRAKE)
        #     self.bot.drive_time(0, 90, 1000)
        self.bot.follow_line((stopCondition))