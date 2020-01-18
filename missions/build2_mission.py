from pybricks import ev3brick as brick
from pybricks.tools import print, wait, StopWatch
from pybricks.parameters import Stop
from sandwichbot import SandwichBot

class Build2Mission():
    """
    Class to send sandwich to black circle.
    """
    IMAGE_PATH = "assets/crane.jpg"

    def __init__(self, bot:SandwichBot):
        self.image_path = Build2Mission.IMAGE_PATH
        self.bot = bot

    def run(self):
        brick.sound.beep()
        self.bot.drive_distance(900, 100)
        self.bot.drive_distance(-200, 100)
        self.bot.attachment_motor.run_angle(360*3, 1500, Stop.BRAKE, False)
        self.bot.turn_to(25)
        self.bot.drive_distance(220, 100)
        self.bot.attachment_motor.run_angle(360*3, -1000, Stop.BRAKE, True)
        self.bot.attachment_motor.run_angle(360*3, 1000, Stop.BRAKE, False)
        self.bot.drive_time(-200,90,1000)
        brick.sound.beep(1000,150,50)
        self.bot.drive_distance(-1000, 200)
