import time
import sys
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

        if sys.platform in ['Windows', 'win32', 'cygwin']:
            if self.configs.newTabAds:
                print()
                print("To use the function 'ad in a new tab' Brave must be in focus")

        i = 15
        while i >= 0:
            print(i, "second(s) to start", end="\r")
            i -= 1
            time.sleep(1)

        print()

        while True:
            if self.configs.check_pixel() is True:
                self.configs.open_brave_notify()

            if sys.platform in ['Windows', 'win32', 'cygwin']:
                if "Brave" in self.utilities.check_fouc():
                    if self.configs.newTabAds:
                        self.configs.open_brave_new_tab()

            time.sleep(1)

    def get_count_ads(self):
        return self.configs.countAds

    def get_count_new_tab_ads(self):
        return self.configs.countNewTabAds