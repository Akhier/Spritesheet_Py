__version__ = "0.0.1"
__author__ = "Akhier Dragonheart"
__license__ = "MIT"


import json
import pygame


def get_spritesheet(jsonpath):
    with open(jsonpath) as jsondata:
        sheetdata = json.load(jsondata)
    try:
        fullimage = pygame.image.load(sheetdata['file']).convert()
    except FileNotFoundError:
        print(sheetdata['file'] + " not found")
