from pybricks import ev3brick as brick
from pybricks.tools import print, wait, StopWatch
from pybricks.parameters import Stop
from sandwichbot import SandwichBot

class TrafficMission():
    """
    Class to lift traffic module.
    """
    IMAGE_PATH = "assets/swing.jpg"

    def __init__(self, bot:SandwichBot):
        self.image_path = TrafficMission.IMAGE_PATH
        self.bot = bot

    def run(self):
        brick.sound.beep()
        self.bot.attachment_motor.reset_angle(0)
        self.bot.drive_distance(120, 50)
        self.bot.drive_distance(200, 100)
        self.bot.drive_distance(700, 200)
        brick.sound.beep(1000,150,50)

        # move arm up while driving to swing
        self.bot.attachment_motor.run_angle(360*3, -1300, Stop.BRAKE, False)

        self.bot.drive_distance(900, 100)
        brick.sound.beep(1000,150,50)
        self.bot.drive_distance(-300, 100)
        self.bot.attachment_motor.run_angle(360*3, -600, Stop.BRAKE, False)
        self.bot.turn_to(-70)
        self.bot.drive_distance(750, 100)
        self.bot.drive_time(-300,300,500)
        #self.bot.drive_distance(-1000, 300)
        # self.bot.follow_line_distance(True, 800)
        brick.sound.beep(1000,150,50)