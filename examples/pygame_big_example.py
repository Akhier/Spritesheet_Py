# encoding=utf8
import sys
sys.path.append("..")
from spritesheet import get_spritesheet
import pygame


def run():
    # Initialize Pygame
    pygame.init()
    window = pygame.display.set_mode((384, 384))
    pygame.display.set_caption("Dragonheart Spritesheet Pygame big example")
    clock = pygame.time.Clock()
    # Get spritesheet
    sprites = get_spritesheet('curses_square.json')
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        window.fill((0, 0, 0))
        i = 0
        for y in range(0, 16):
            for x in range(0, 16):
                window.blit(sprites[str(i)], (x * 24, y * 24))
                i += 1
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    run()
    pygame.quit()
