import pygame
import sys

from pygame.locals import RESIZABLE, QUIT

from core import OrtogonalMaze, Size
from maze.core.utils import Point
from ui import OrtogonalMazeUI

pygame.init()

pygame.display.set_caption("Maze")
pygame.display.set_mode((600, 600), RESIZABLE)

surface = pygame.display.get_surface()
if surface == None: raise ValueError("No surface found")

fps = pygame.time.Clock()

ortogonal_maze = OrtogonalMaze(Size(2, 2))
ortogonal_maze_ui = OrtogonalMazeUI(ortogonal_maze)

# TODO: add more consistent tests
ortogonal_maze.add_wall(Point(0, 0), Point(0, 1))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    ortogonal_maze_ui.draw_to(surface)

    pygame.display.update()
    fps.tick(60)
