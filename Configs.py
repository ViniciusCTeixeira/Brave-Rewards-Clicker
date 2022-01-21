import pyautogui
import sys
import time

from Utilities import Utilities


class Configs:
    def __init__(self):
        self.braveIconColor1 = None
        self.braveIconColor2 = None
        self.braveIconPosition1 = None
        self.braveIconPosition2 = None
        self.screenSize = None
        self.countAds = 0
        self.version = 1.5
        self.utilities = Utilities()

    def check_config(self):
        print("Loading settings ...")
        time.sleep(1)
        if self.utilities.settings_file_exist() is True:
            if self.utilities.settings_file_version(self.version) is True:
                self.load_config()
            else:
                self.create_config()
        else:
            self.create_config()

        print("Running ...")

    def load_config(self):
        print("Settings loaded!")
        data = self.utilities.load_file(self.utilities.settingsPath, True)
        self.braveIconColor1 = data['data']['braveIconColor1']
        self.braveIconColor2 = data['data']['braveIconColor2']
        self.braveIconPosition1 = data['data']['braveIconPosition1']
        self.braveIconPosition2 = data['data']['braveIconPosition2']
        self.screenSize = data['data']['screenSize']

    def create_config(self):
        print("Settings not found!")
        time.sleep(1)
        print("Creating settings ...")
        time.sleep(1)
        input("Hover over the orange part of the notification icon and press the Enter key")
        self.braveIconPosition1 = pyautogui.position()
        self.braveIconColor1 = pyautogui.screenshot().getpixel(self.braveIconPosition1)
        input("Hover over the white part of the notification icon and press the Enter key")
        self.braveIconPosition2 = pyautogui.position()
        self.braveIconColor2 = pyautogui.screenshot().getpixel(self.braveIconPosition2)
        self.screenSize = pyautogui.size()
        print("Creating settings file ...")
        time.sleep(1)
        data = {
            "v": self.version,
            "data": {
                "braveIconColor1": self.braveIconColor1,
                "braveIconPosition1": self.braveIconPosition1,
                "braveIconColor2": self.braveIconColor2,
                "braveIconPosition2": self.braveIconPosition2,
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
            pix_val1 = pyautogui.pixel(self.braveIconPosition1[0], self.braveIconPosition1[1])
            pix_val2 = pyautogui.pixel(self.braveIconPosition2[0], self.braveIconPosition2[1])
        except IOError:
            print("Cannot get pixel for the moment")
            pix_val1 = (0, 0, 0)
            pix_val2 = (0, 0, 0)

        if pix_val1 == self.braveIconColor1 and pix_val2 == self.braveIconColor2:
            return True
        else:
            return False

    def open_brave_notify(self):
        print("Opening ad ...")
        pyautogui.moveTo(self.braveIconPosition1[0], self.braveIconPosition1[1], duration=2)
        pyautogui.click(interval=5, button='left', clicks=2)
        pyautogui.moveTo(self.screenSize[0] / 2, self.screenSize[1] / 2, duration=2)
        time.sleep(10)
        pyautogui.scroll(10)
        pyautogui.hotkey('ctrl', 'w')
        self.countAds += 1
        print("Ads:", self.countAds)
