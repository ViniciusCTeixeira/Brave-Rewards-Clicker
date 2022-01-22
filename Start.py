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

        if self.configs.newTabAds:
            print("Open Brave to use ads in new tab")
            i = 15
            while i > 0:
                print(i, "second(s) to start", end="\r")
                i -= 1
                time.sleep(1)

            print()

        while True:
            if self.configs.check_pixel() is True:
                self.configs.open_brave_notify()
            if self.configs.newTabAds:
                self.configs.open_brave_new_tab()
            time.sleep(1)

    def get_count_ads(self):
        return self.configs.countAds

    def get_count_new_tab_ads(self):
        return self.configs.countNewTabAds