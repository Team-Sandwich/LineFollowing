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