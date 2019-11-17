from sandwichbot import SandwichBot

class BuildMission():
    IMAGE_PATH = "assets/build.jpg"

    def __init__(self, bot:SandwichBot):
        self.image_path = BuildMission.IMAGE_PATH
        self.bot = bot

    def run(self):
        pass