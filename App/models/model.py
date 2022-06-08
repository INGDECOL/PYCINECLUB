import json

import App.config as conf


class Db:
    def __init__(self):
        self.chemin = conf.DATA_FILE_DIR

    def write(self, data):
        with open(self.chemin, "w") as f:
            json.dump(data, f, indent=4)


def get_data():
    with open(conf.DATA_FILE_DIR, "r") as f:
        return json.load(f)
