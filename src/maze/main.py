import pygame
import sys

from pygame.locals import * # type: ignore

from core import Maze
from views import MazeView

pygame.init()

# Window Configs
pygame.display.set_caption("Maze")
pygame.display.set_mode((800, 600), RESIZABLE)

surface = pygame.display.get_surface()
if surface == None: raise ValueError("No surface found")

fps = pygame.time.Clock()

mazeview = MazeView(surface, Maze((0, 0)))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    mazeview.draw()

    pygame.display.update()
    fps.tick(60)
