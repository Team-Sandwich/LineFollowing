from pybricks import ev3brick as brick
from pybricks.tools import print, wait, StopWatch
from sandwichbot import SandwichBot

class BuildMission():
    """
    Class to send tower to red circle.
    """
    IMAGE_PATH = "assets/build.jpg"

    def __init__(self, bot:SandwichBot):
        self.image_path = BuildMission.IMAGE_PATH
        self.bot = bot

    def run(self):
        brick.sound.beep()
        print("Run Build Mission")
        self.bot.drive_distance(1237,150)
        self.bot.drive_distance(-300,100)
        self.bot.drive_time(-100,30,1000)
        self.bot.drive_distance(-1600, 400)

        

        