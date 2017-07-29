__version__ = "0.0.1"
__author__ = "Akhier Dragonheart"
__license__ = "MIT"


import json


def get_spritesheet(jsonpath):
    with open(jsonpath) as jsondata:
        sheetdata = json.load(jsondata)
