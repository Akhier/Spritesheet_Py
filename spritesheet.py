__version__ = "0.1.0"
__author__ = "Akhier Dragonheart"
__license__ = "MIT"


import json
import pygame


def get_spritesheet(jsonpath):
    '''Get a spritesheet though data stored in a json file

    This function expects all sprites to be the same size. Along with that it
    needs your json file to have a 'file' with the location of the image
    to get the sprites from, 'sprite_width' and 'sprite_height' to define the
    size of the sprites you want, 'colorkey' which should either be the color
    you want keyed, -1 which will grab the top left pixels color to use, or
    false if you don't want a color keyed, and finally 'sprites' which contains
    each row of your tileset in order which themselves need to contain 'id'
    which is the name of the sprite and in the order they appear in the row
    For an example of this:
    {
    "file": "examplesheet.png",
    "colorkey": false,
    "sprite_width":50,
    "sprite_height":50,
    "sprites": [
            {
                "id": "yellow",
                "id": "blue",
                "id": "purple"
            },
            {
                "id": "green",
                "id": "red"
            }
        ]
    }

    :param jsonpath: This is were the json file detailing your
    spritesheet is located
    :return: Dictionary containing pairs of (sprite_name, sprite_image)
    '''
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
