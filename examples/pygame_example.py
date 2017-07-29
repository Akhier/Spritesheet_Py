import sys
sys.path.append("..")
from spritesheet import get_spritesheet
import pygame


def run():
    # Initialize Pygame
    pygame.init()
    window = pygame.display.set_mode((190, 130))
    pygame.display.set_caption("Dragonheart Spritesheet Pygame example")
    clock = pygame.time.Clock()
    # Get spritesheet
    sprites = get_spritesheet('example.json')
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        window.fill((0, 0, 0))
        window.blit(sprites['yellow'], (10, 10))
        window.blit(sprites['blue'], (70, 10))
        window.blit(sprites['purple'], (130, 10))
        window.blit(sprites['green'], (10, 70))
        window.blit(sprites['red'], (70, 70))
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    run()
    pygame.quit()
