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

        # prepreation
        self.bot.attachment_motor.reset_angle(0)
        self.bot.attachment_motor.run_angle(360*3, -360*3, Stop.BRAKE, False)

        # driving to swing
        self.bot.drive_distance(1647, 200)
        self.bot.stop(Stop.BRAKE)
        self.bot.turn_to(60)
        self.bot.drive_distance(210, 75)
        self.bot.stop(Stop.BRAKE)
        self.bot.turn_to(-60)
        self.bot.drive_distance(250, 250)
        self.bot.stop(Stop.BRAKE)
        self.bot.drive_distance(-200, 75)
        self.bot.stop(Stop.BRAKE)
        brick.sound.beep()

        # turning to the eleavator
        self.bot.turn_to(-62)

        # driving to the eleavator
        self.bot.drive_distance(750, 234)
        self.bot.stop()
        wait(1000)

        # lifting up robot arm
        self.bot.attachment_motor.run_angle(360*3, -360*2, Stop.BRAKE, True)

        # backing up from eleavator
        self.bot.drive_distance(-300, 75)
        self.bot.attachment_motor.run_angle(360*3, 360*5, Stop.BRAKE, True)
        self.bot.turn_to(60)
        self.bot.drive_distance(-3000, 500)
        
