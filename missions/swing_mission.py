from pybricks import ev3brick as brick
from pybricks.tools import print, wait, StopWatch
from sandwichbot import SandwichBot

class SwingMission():
    IMAGE_PATH = "assets/swing.jpg"

    def __init__(self, bot:SandwichBot):
        self.image_path = SwingMission.IMAGE_PATH
        self.bot = bot

    def run(self):
        brick.sound.beep()
        print("Run Swing Mission")