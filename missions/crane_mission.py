from pybricks import ev3brick as brick
from pybricks.tools import print, wait, StopWatch
from pybricks.parameters import Stop
from sandwichbot import SandwichBot

class CraneMission():
    IMAGE_PATH = "assets/crane.jpg"

    def __init__(self, bot:SandwichBot):
        self.image_path = CraneMission.IMAGE_PATH
        self.bot = bot

    def run(self):
        brick.sound.beep()
        print("Run Crane Mission")

        self.bot.drive_distance(775,100)
        self.bot.attachment_motor.run_angle(360*3, -360*2, Stop.BRAKE, True)
        wait(300)
        self.bot.attachment_motor.run_angle(360*3, 360*2, Stop.BRAKE, True)
        self.bot.turn_to(90)
        self.bot.attachment_motor.run_angle(360*3, -360*5, Stop.BRAKE, False)
        self.bot.drive_distance(-1000, 200)
