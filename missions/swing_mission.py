from pybricks import ev3brick as brick
from pybricks.tools import print, wait, StopWatch
from pybricks.parameters import Stop
from sandwichbot import SandwichBot

class SwingMission():
    IMAGE_PATH = "assets/swing.jpg"

    def __init__(self, bot:SandwichBot):
        self.image_path = SwingMission.IMAGE_PATH
        self.bot = bot

    # starting the swing & eleavator missions
    def run(self):
        brick.sound.beep()
        print("Run Swing Mission")

        # move arm up while driving to swing
        self.bot.attachment_motor.reset_angle(0)
        self.bot.attachment_motor.run_angle(360*3, -360*3, Stop.BRAKE, False)

        # driving to swing
        self.bot.drive_distance(247, 50)
        self.bot.drive_distance(1400, 150)
        self.bot.stop(Stop.BRAKE)
        self.bot.turn_to(58)
        self.bot.drive_distance(210, 75)
        self.bot.stop(Stop.BRAKE)
        self.bot.turn_to(-60)
        self.bot.drive_distance(250, 250)
        self.bot.stop(Stop.BRAKE)
        self.bot.drive_distance(-200, 75)
        self.bot.stop(Stop.BRAKE)
        brick.sound.beep()

        self.bot.turn_to(60)

        self.bot.drive_distance(-200, 120)
        self.bot.turn_to(-60)

        self.bot.drive_distance(-100, 50)
        self.bot.drive_distance(-3000, 500)
        self.bot.attachment_motor.run_angle(360*3, -360*2, Stop.BRAKE, False)

        
