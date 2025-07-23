import pygame
import sys

from pygame.locals import RESIZABLE, QUIT

from core import OrtogonalMaze, Size
from core.utils import Point
from ui import OrtogonalMazeUI

pygame.init()

pygame.display.set_caption("Maze")
pygame.display.set_mode((600, 600), RESIZABLE)

surface = pygame.display.get_surface()
if surface == None: raise ValueError("No surface found")

fps = pygame.time.Clock()

maze = OrtogonalMaze(Size(5, 5))
maze_ui = OrtogonalMazeUI(maze)

# TODO: add more consistent tests
maze.remove_wall(Point(0, 0), Point(1, 0))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    maze_ui.draw_to(surface)

    pygame.display.update()
    fps.tick(60)
