import os
import darkdetect
import pyautogui
import time
from datetime import datetime
from Utilities import Utilities


class Configs:
    def __init__(self):
        self.screenSize = None
        self.newTabAdsPosition = None
        self.brave = None
        self.theme = None
        self.newTabAds = 0
        self.countAds = 0
        self.countNewTabAds = 0
        self.version = 1.7
        self.utilities = Utilities()

        if darkdetect.isDark():
            self.brave = b'iVBORw0KGgoAAAANSUhEUgAAADwAAAAZCAYAAABtnU33AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAANUSURBVFhH7ZhfSFRZHMc/4/bHaSNqY3BI3fLFEI1AZGIJNxLsIVZEKJReAoMeUkJCQTZElH1ZfVCWaKEHsR5SKbDJzQeNQi2kgYhMUawQGpukdlaxbEZqZzrnN+eSeCvSh8BpPjCcc37nd4f5/n7fey53HGlpaVG+I5LM+N2QEBzvJARb7HVG8P/swL/jf/yuEP5t85StC5vdtYtN8MFtYZ7lvuafHRtN5OMh3py8gH99gKNJCyay9rA9liY8z/lx4zq4+BrWW6INkQjs2ULk7QI736eZ4Nfh9/vNDGZnZ/F6vdTV1ZnIt8PW4eQkpb/pISyqLv6+D67+Cbeuw6EcePkC7j4jyWGSV0h9fT3p6ekitrS01ES/LTbBUZSaiTuw+Sf4YxhyfgXPAfD6wJ0KD+4tdfmqSE1NZWZmxqxi3W9ra5PR4/HIfHJyUtaDg4MoF1JUVMTIyIi5IoZe63y9r4uo8/V1HR0dJsOOTXD/bDJcOAnjQ/DoJgQDSqQSfuMKPJmAE4d5yAaTvTIaGhrkR+Xl5dHe3m6iMZxOp3Tf5/PR3d1NZmamrLX9Gxsb6enpIRwOU15eLvnV1dXMzc1JfnNzM8FgUPILCgqkoLpAn8Im2PvvpthEd3nvIdj9C6TvgiPHYXpKuuuNmJwVYlm6tbWV2tpa6Y5FTU2NmYHL5aKvr0/E5ObmmigMDw9TXFws8/z8fAYGBmSenZ1NYWGhFFPnZGRkUFJSInvLsQnu+091WHOjBW63wd+n4HyjOsTOKYufka1rUaeMq0VbVls6J0edC4bp6WkZdRF0MbTgyspK+vv7Ja7RnczKyhILa1FLDz2rmNbHcsJybILfRR2xW3T+FfiuQZ36NF1WHX8ET5WlFa+iP8i4WvSPcbvdjI6OmshHUlJSxLqdnZ0EAgFbUcbHx6VgY2NjJgpTU1OUlZVJITTa7p/DJlhz+rE6sDT3e+CYCwp3QucFCf0V3SLjarDu4aqqKrq6usSyy9H3qhajrdnb2yv36VKGhoakyy0tyoGGiooKQqGQXKO/X9vdEr+cz74e/rY9xPnMII43aqEfoWo8G9nKpchm2V+rfPF9WD9vB3fPkByIsn/ezaJ+ZK1xEn8AxDsJwfFOQnC8kxAc38AHDgBFfkS4iUUAAAAASUVORK5CYII='
        else:
            self.brave = b'iVBORw0KGgoAAAANSUhEUgAAAD8AAAAZCAYAAACGqvb0AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAANgSURBVFhH7ZhfSNNRFMe/q9SHRnNFEkzNl/BhbpKEIUJ7iMYcJYiGFoigNCSRQe4lIQMVIVFCiiKDwRBsWIglUwQptEQyNGqMFBKhJGGRiWvlNtPuPbsDs58zDQr77QM/zv2de+5v+557zt0fxfz8/Cpkyi5hZUlMvFyJiZcrUcXvmX4N9elMqE1aqE8egdqQhoTee2J25yP5URfnGYSyxQIsqIHQMrAcYpZdERsMwH/1BoJnzokVOxNJ8YnWVCiWA4DDxzKRILyClRVAtw8ILOHzi4/C+XtotVoxAlJSUmC1WpGXlyc8fx/JslcEvwHNr5hAP1B7HHhwDXj8CDBmAN45YOQdS8J3Eb01Ojo64PF4SHh9fb3w/huke17B3JPPAOV+oHEUyDgBZBuAh2PAIQ3w8jnwh98L5+bmoNPpxF24Kux2O9nZ2Vka5+Tk0L3FYsHCwgKmpqZgMpnEijD8nsfz+YaGBorn69ra2kTExkiKD+nZC7Sznn/zFHAPAp8+MMEsCa77wNtJoMKMZe1REb01SktL6Q12dXWhsrJSeMP4fD6qiuTkZOTm5mJ0dJTueYt0d3cjPT0dKpUKExMTFD88PIzU1FSKdzgc0Gg0FN/f30+WJysakuKD2YXhAd/9TCOQnsOaNA0oKgNmZ2jXQyYRs0UiZd/U1ISqqiratQhlZez5Ar/fD5vNhuLiYjidTuEFCgsL4XK5aDw0NISCggIac8Gtra2UWJ64kZERuqIhLT5THEKu68ATO3D7InCL9afjJmuDSzQVNBWR3S5ZWVlU9l6vV3jYQZuYSJYnhCcmPz+fBNXU1JCfYzQa0dfXR2XOxa09MCOJjVzl5eViRhrpnt8dx/peASyy03ysB7jCruZOVgluYJqVPWPlQBLZ7cJL1+12Iynp1+fwXeflrdfroVQqMTAwIGbCCTKbzWhsbPxJON/tzs5OSgqHt8RmSItn+MvvhAfjvcD5g8Cpw4CznVxLF2xkt0Ok52tra1FXV0f9uh7e21wYF1RSUkI9vxaDwUBlzlsgQnV1NSWMr+HP5y0RScRGRP09Hz/eg713K9hJxELeM8cX4OvlFgTORi+nncLmf2asrkBlOwbMLGHR+RKr8eu+9OxgNhf/H7Nhz8uBmHi5EhMvV2QsHvgBnR9Na+n1NKYAAAAASUVORK5CYII='

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
        if data is not False:
            try:
                if bool(data['data']['screenSize']):
                    self.screenSize = data['data']['screenSize']
                else:
                    print("Settings are invalid!!!")
                    self.create_config()

                if bool(data['data']['theme']):
                    if data['data']['theme'] is darkdetect.theme():
                        self.theme = data['data']['theme']
                    else:
                        print("Settings are invalid!!!")
                        self.create_config()
                else:
                    print("Settings are invalid!!!")
                    self.create_config()

                if bool(data['data']['newTabAds']):
                    self.newTabAds = data['data']['newTabAds']
                    self.newTabAdsPosition = data['data']['newTabAdsPosition']

                print("Settings loaded!")
            except KeyError:
                print("Settings are invalid!!!")
                self.create_config()
        else:
            print("Settings are invalid!!!")
            self.create_config()

    def create_config(self):
        time.sleep(1)
        print("Creating settings ...")
        time.sleep(1)
        self.theme = darkdetect.theme()
        self.screenSize = pyautogui.size()
        newTab = input("Ads in new tab? y/n:")
        if newTab == "y":
            self.newTabAds = 1
            input("Hover over the link part of the new page and press the Enter key")
            self.newTabAdsPosition = pyautogui.position()
        print("Creating settings file ...")
        time.sleep(1)
        data = {
            "v": self.version,
            "data": {
                "screenSize": self.screenSize,
                "theme": self.theme,
                "newTabAds": self.newTabAds,
                "newTabAdsPosition": self.newTabAdsPosition
            }
        }
        if self.utilities.create_file(self.utilities.settingsPath, data, True) is False:
            if os.path.exists(self.utilities.settingsPath):
                os.remove(self.utilities.settingsPath)
            print("Error on creating the file!!!")
            exit(1)
        elif self.utilities.create_file_image(self.utilities.settingsImagePath, self.brave) is False:
            if os.path.exists(self.utilities.settingsImagePath):
                os.remove(self.utilities.settingsImagePath)
            print("Error on creating the file!!!")
            exit(1)
        else:
            print("Created in: ", self.utilities.settingsPath)
            print("Created in: ", self.utilities.settingsImagePath)

    def open_brave_new_tab(self):
        self.countNewTabAds += 1
        now = datetime.now()
        print("Opening new tab:", now.strftime("%d/%m/%Y %H:%M:%S"))
        pyautogui.moveTo(self.screenSize[0] / 2, self.screenSize[1] / 2, duration=1)
        pyautogui.hotkey('ctrl', 't')
        time.sleep(5)
        pyautogui.moveTo(self.newTabAdsPosition[0], self.newTabAdsPosition[1], duration=1)
        pyautogui.click(button='left', clicks=1)
        pyautogui.moveTo(self.screenSize[0] / 2, self.screenSize[1] / 2, duration=1)
        time.sleep(5)
        pyautogui.scroll(-5000)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'w')

    def check_pixel(self):
        now = datetime.now()
        cord = pyautogui.locateOnScreen('brave.png', confidence=0.9)
        if cord:
            print("Pixel obtained for the moment:", now.strftime("%d/%m/%Y %H:%M:%S"))
            return cord
        else:
            print("Cannot get pixel for the moment:", now.strftime("%d/%m/%Y %H:%M:%S"), end="\r")
            return False

    def open_brave_notify(self, cord):
        self.countAds += 1
        now = datetime.now()
        print("Opening ad:", now.strftime("%d/%m/%Y %H:%M:%S"))
        cord = pyautogui.center(cord)
        pyautogui.moveTo(cord.x, cord.y, duration=1)
        pyautogui.click(interval=2, button='left', clicks=2)
        pyautogui.moveTo(self.screenSize[0] / 2, self.screenSize[1] / 2, duration=1)
        time.sleep(5)
        pyautogui.scroll(-5000)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'w')
