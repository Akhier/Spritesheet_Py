from spritesheet import get_spritesheet
import pygame
import pytest
import os


@pytest.fixture
def setup():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    pygame.init()
    pygame.display.set_mode((1, 1))


def test_get_spritesheet_return_type(setup):
    output = get_spritesheet('tests/test.json')
    assert type(output) == dict


def test_get_spritesheet_gets_all_sprites(setup):
    output = get_spritesheet('tests/test.json')
    assert len(output.keys()) == 5


def test_get_spritesheet_contains_surfaces(setup):
    output = get_spritesheet('tests/test.json')
    assert type(output['red']) == pygame.Surface
    assert type(output['green']) == pygame.Surface
