from pybricks import ev3brick as brick
from pybricks.tools import print, wait, StopWatch
from pybricks.parameters import Stop
from sandwichbot import SandwichBot

class SwingMission():
    """
    Class to tackle Swing Mission.
    """
    IMAGE_PATH = "assets/swing.jpg"

    def __init__(self, bot:SandwichBot):
        self.image_path = SwingMission.IMAGE_PATH
        self.bot = bot

    def run(self):
        """
        Start the swing mission.
        """
        brick.sound.beep()
        print("Run Swing Mission")

        # move arm up while driving to swing
        self.bot.attachment_motor.reset_angle(0)
        self.bot.attachment_motor.run_angle(360*3, -900, Stop.BRAKE, False)

        # driving to swing
        # self.bot.drive_distance(1647, 200)
        # self.bot.stop(Stop.BRAKE)

        self.bot.drive_distance(847, 200)
        self.bot.follow_line_distance(True, 800)
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
        brick.sound.beep(1000, 150, 50)

        self.bot.drive_time(-90,60,1200)
        self.bot.drive_time(-90,-60,1000)

        # self.bot.turn_to(60)
        # self.bot.drive_distance(-300, 120)
        # self.bot.turn_to(-60)

        self.bot.attachment_motor.run_angle(360*3, -360*2, Stop.BRAKE, False)
        self.bot.drive_distance(-2200, 400)
