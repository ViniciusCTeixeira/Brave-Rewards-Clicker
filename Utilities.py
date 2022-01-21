import json
import os


class Utilities:
    def __init__(self):
        self.rootPath = os.path.abspath(os.path.join(os.path.dirname(__file__), "src", ".."))
        self.settingsPath = os.path.join(self.rootPath, "settings.json")

    def settings_file_exist(self):
        return os.path.exists(self.settingsPath)

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
                data = json.loads(f.read())

            if isJson is False:
                data = f.read()

            f.close()

            return data
        except IOError:
            return False
