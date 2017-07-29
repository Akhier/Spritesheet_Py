__version__ = "0.0.1"
__author__ = "Akhier Dragonheart"
__license__ = "MIT"


import json
import pygame


def get_spritesheet(jsonpath):
    with open(jsonpath) as json_data:
        sheet_data = json.load(json_data)
    try:
        full_image = pygame.image.load(sheet_data['file']).convert()
    except FileNotFoundError:
        print(sheet_data['file'] + " not found")
    color_key = sheet_data['color_key']
    sprite_width = sheet_data['sprite_width']
    sprite_height = sheet_data['sprite_height']
    for row in sheet_data['sprites']:
        for sprite_name in row:
            pass
