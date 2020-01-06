from pybricks import ev3brick as brick
from pybricks.tools import print, wait, StopWatch
from sandwichbot import SandwichBot

class TrafficMission():
    """
    Class to lift traffic module.
    """
    IMAGE_PATH = "assets/ramp.jpg"

    def __init__(self, bot:SandwichBot):
        self.image_path = TrafficMission.IMAGE_PATH
        self.bot = bot

    def run(self):
        brick.sound.beep()
        self.bot.drive_distance(1126, 250)
        self.bot.turn_to(5)
        self.bot.drive_distance(-2250, 450)
        brick.sound.beep(1000,150,50)