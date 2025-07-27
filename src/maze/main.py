import pygame
import sys

from pygame.locals import RESIZABLE, QUIT

pygame.init()

pygame.display.set_caption("Maze")
pygame.display.set_mode((750, 750), RESIZABLE)

surface = pygame.display.get_surface()
if surface == None: raise ValueError("No surface found")

fps = pygame.time.Clock()

loop = False
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fps.tick(60)