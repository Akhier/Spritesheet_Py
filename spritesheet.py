__version__ = "0.0.2"
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
    colorkey = sheet_data['colorkey']
    sprite_width = sheet_data['sprite_width']
    sprite_height = sheet_data['sprite_height']
    sprites = {}
    y = 0
    for row in sheet_data['sprites']:
        x = 0
        for sprite_name in row:
            rect = pygame.Rect(x, y, sprite_width, sprite_height)
            sprite = pygame.Surface(rect.size).convert()
            sprite.blit(full_image, (0, 0), rect)
            if colorkey:
                if colorkey is -1:
                    colorkey = sprite.get_at((0, 0))
                sprite.set_colorkey(colorkey, pygame.RLEACCEL)
            sprites[sprite_name] = sprite
            x += sprite_width
        y += sprite_height
    return sprites
