import base64
import json
import os
import win32gui


class Utilities:
    def __init__(self):
        self.rootPath = os.path.abspath(os.curdir)
        self.settingsPath = os.path.join(self.rootPath, "settings.json")
        self.settingsImagePath = os.path.join(self.rootPath, "brave.png")

    def settings_file_exist(self):
        if os.path.exists(self.settingsPath):
            if os.path.exists(self.settingsImagePath):
                return True
            else:
                return False
        else:
            return False

    def settings_file_version(self, version):
        try:
            f = open(self.settingsPath, "r")

            try:
                data = json.loads(f.read())
            except json.decoder.JSONDecodeError:
                return False

            f.close()

            try:
                if data['v'] == version:
                    return True
                else:
                    return False
            except KeyError:
                return False
        except IOError:
            return False

    @staticmethod
    def create_file(path, content, isJson=False):
        try:
            f = open(path, 'w')
            if isJson is True:
                json.dump(content, f)

            if isJson is False:
                f.write(content)

            f.close()
        except IOError:
            return False

    @staticmethod
    def create_file_image(path, content):
        try:
            f = open(path, 'wb')
            f.write(base64.b64decode((content)))
            f.close()
        except IOError:
            return False

    @staticmethod
    def load_file(path, isJson=False):
        try:
            f = open(path, "r")
            data = None
            if isJson is True:
                try:
                    data = json.loads(f.read())
                except json.decoder.JSONDecodeError:
                    return False

            if isJson is False:
                data = f.read()

            f.close()

            return data
        except IOError:
            return False

    @staticmethod
    def check_fouc():
        active_window_name = None
        window = win32gui.GetForegroundWindow()
        active_window_name = win32gui.GetWindowText(window)

        return active_window_name
