import pyautogui
import time
from datetime import datetime
from Utilities import Utilities


class Configs:
    def __init__(self):
        self.braveIconColor1 = None
        self.braveIconColor2 = None
        self.braveIconPosition1 = None
        self.braveIconPosition2 = None
        self.screenSize = None
        self.newTabAds = 0
        self.countAds = 0
        self.countNewTabAds = 0
        self.version = 1.5
        self.utilities = Utilities()

    def check_config(self):
        print("Loading settings ...")
        time.sleep(1)
        if self.utilities.settings_file_exist() is True:
            if self.utilities.settings_file_version(self.version) is True:
                self.load_config()
            else:
                print("Settings are invalid!!!")
                self.create_config()
        else:
            print("Settings not found!")
            self.create_config()

        time.sleep(1)
        print("Running ...")

    def load_config(self):
        data = self.utilities.load_file(self.utilities.settingsPath, True)
        try:
            if bool(data['data']['braveIconColor1']):
                self.braveIconColor1 = data['data']['braveIconColor1']
            else:
                print("Settings are invalid!!!")
                self.create_config()

            if bool(data['data']['braveIconColor2']):
                self.braveIconColor2 = data['data']['braveIconColor2']
            else:
                print("Settings are invalid!!!")
                self.create_config()

            if bool(data['data']['braveIconPosition1']):
                self.braveIconPosition1 = data['data']['braveIconPosition1']
            else:
                print("Settings are invalid!!!")
                self.create_config()

            if bool(data['data']['braveIconPosition2']):
                self.braveIconPosition2 = data['data']['braveIconPosition2']
            else:
                print("Settings are invalid!!!")
                self.create_config()

            if bool(data['data']['screenSize']):
                self.screenSize = data['data']['screenSize']
            else:
                print("Settings are invalid!!!")
                self.create_config()

            if bool(data['data']['newTabAds']):
                self.newTabAds = data['data']['newTabAds']

            print("Settings loaded!")
        except KeyError:
            print("Settings are invalid!!!")
            self.create_config()

    def create_config(self):
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
        newTab = input("Ads in new tab? y/n")
        if newTab == "y":
            self.newTabAds = 1
        print("Creating settings file ...")
        time.sleep(1)
        data = {
            "v": self.version,
            "data": {
                "braveIconColor1": self.braveIconColor1,
                "braveIconPosition1": self.braveIconPosition1,
                "braveIconColor2": self.braveIconColor2,
                "braveIconPosition2": self.braveIconPosition2,
                "screenSize": self.screenSize,
                "newTabAds": self.newTabAds
            }
        }
        if self.utilities.create_file(self.utilities.settingsPath, data, True) is False:
            print("Error on creating the file!!!")
            exit(1)
        else:
            print("Created in: ", self.utilities.settingsPath)

    def open_brave_new_tab(self):
        now = datetime.now()
        print("Opening new tab:", now.strftime("%d/%m/%Y %H:%M:%S"))
        pyautogui.moveTo(self.screenSize[0] / 2, self.screenSize[1] / 2)
        pyautogui.hotkey('ctrl', 't')
        pyautogui.click(button='left', clicks=1)
        time.sleep(4)
        pyautogui.hotkey('ctrl', 'w')
        self.countNewTabAds += 1

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
        now = datetime.now()
        print("Opening ad:", now.strftime("%d/%m/%Y %H:%M:%S"))
        pyautogui.moveTo(self.braveIconPosition1[0], self.braveIconPosition1[1], duration=1)
        pyautogui.click(interval=2, button='left', clicks=2)
        pyautogui.moveTo(self.screenSize[0] / 2, self.screenSize[1] / 2, duration=1)
        time.sleep(10)
        pyautogui.scroll(-10)
        pyautogui.hotkey('ctrl', 'w')
        self.countAds += 1
