import json
import os
import sys


class Utilities:
    def __init__(self):
        self.rootPath = os.path.abspath(os.curdir)
        self.settingsPath = os.path.join(self.rootPath, "settings.json")

    def settings_file_exist(self):
        return os.path.exists(self.settingsPath)

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
        if sys.platform in ['Windows', 'win32', 'cygwin']:
            import win32gui
            window = win32gui.GetForegroundWindow()
            active_window_name = win32gui.GetWindowText(window)

        return active_window_name
