import pygame
import sys

from pygame.locals import * # type: ignore

pygame.init()

# Window Configs
pygame.display.set_caption("Maze")
pygame.display.set_mode((800, 600), RESIZABLE)

surface = pygame.display.get_surface()
fps = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fps.tick(60)
