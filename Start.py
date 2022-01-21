import time
from Configs import Configs
from Utilities import Utilities


class Main:
    def __init__(self):
        self.utilities = Utilities()
        self.configs = Configs()

    def start(self):
        print("Thank you for using Brave Rewards Clicker!!!")
        time.sleep(1)
        self.configs.check_config()

        while True:
            if self.configs.check_pixel() is True:
                self.configs.open_brave_notify()
            time.sleep(5)
