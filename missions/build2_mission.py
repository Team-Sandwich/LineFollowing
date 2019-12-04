from pybricks import ev3brick as brick
from pybricks.tools import print, wait, StopWatch
from sandwichbot import SandwichBot

class Build2Mission():
    IMAGE_PATH = "assets/build2.jpg"

    def __init__(self, bot:SandwichBot):
        self.image_path = Build2Mission.IMAGE_PATH
        self.bot = bot

    def run(self):
        brick.sound.beep()
        self.bot.drive_distance(900, 100)
        self.bot.drive_distance(-900, 100)
