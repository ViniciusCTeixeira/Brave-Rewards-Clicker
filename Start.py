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
            print()
            time.sleep(5)

        while True:
            if self.configs.newTabAds:
                self.configs.open_brave_new_tab()

            if self.configs.check_pixel() is True:
                self.configs.open_brave_notify()
            time.sleep(1)

    def get_count_ads(self):
        return self.configs.countAds

    def get_count_new_tab_ads(self):
        return self.configs.countNewTabAds