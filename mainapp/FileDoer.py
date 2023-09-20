import json
import os

work_dir = os.getcwd()


class FileDoer:
    def __init__(self, file_name):
        self.file_name = work_dir + '/' + file_name

    def read_file(self):
        try:
            with open(self.file_name, 'r').read().splitlines() as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def write_file(self, object_python):
        with open(self.file_name, 'w') as file:
            json.dump(object_python, file, indent=4)
