import pyautogui
import sys
import time

from Utilities import Utilities


class Configs:
    def __init__(self):
        self.braveIconColor = None
        self.braveIconPosition = None
        self.screenSize = None
        self.countAds = 0
        self.utilities = Utilities()

    def check_config(self):
        print("Loading settings ...")
        time.sleep(1)
        if self.utilities.settings_file_exist() is True:
            self.load_config()
        else:
            self.create_config()

        print("Running ...")

    def load_config(self):
        print("Settings loaded!")
        data = self.utilities.load_file(self.utilities.settingsPath, True)
        self.braveIconColor = data['data']['braveIconColor']
        self.braveIconPosition = data['data']['braveIconPosition']
        self.screenSize = data['data']['screenSize']

    def create_config(self):
        print("Settings not found!")
        time.sleep(1)
        print("Creating settings ...")
        time.sleep(1)
        input("Hover over the orange part of the notification icon and press the Enter key")
        self.braveIconPosition = pyautogui.position()
        self.braveIconColor = pyautogui.screenshot().getpixel(self.braveIconPosition)
        self.screenSize = pyautogui.size()
        print("Creating settings file ...")
        time.sleep(1)
        data = {
            "data": {
                "braveIconColor": self.braveIconColor,
                "braveIconPosition": self.braveIconPosition,
                "screenSize": self.screenSize
            }
        }
        if self.utilities.create_file(self.utilities.settingsPath, data, True) is False:
            print("Error on creating the file!!!")
            exit(1)
        else:
            print("Created in: ", self.utilities.settingsPath)

    def check_pixel(self):
        try:
            pix_val = pyautogui.pixel(self.braveIconPosition[0], self.braveIconPosition[1])
        except IOError:
            print("Cannot get pixel for the moment")
            pix_val = (0, 0, 0)

        if pix_val == self.braveIconColor:
            return True
        else:
            return False

    def open_brave_notify(self):
        pyautogui.moveTo(self.braveIconPosition[0], self.braveIconPosition[1], duration=2)
        pyautogui.click(interval=5, button='left', clicks=2)
        pyautogui.moveTo(self.screenSize[0] / 2, self.screenSize[1] / 2, duration=2)
        time.sleep(10)
        pyautogui.scroll(10)
        pyautogui.hotkey('ctrl', 'w')
        self.countAds += 1
        print("Total Ads:", self.countAds)
