import pygame
import sys

from pygame.locals import RESIZABLE, QUIT, K_SPACE

from core.maze import GridMaze, GridIndex
from ui.mazeui import GridMazeUI
from core.utils import Size
from core.generators import DepthFirstGenerator

from locals import BLACK

pygame.init()

pygame.display.set_caption("Maze")
pygame.display.set_mode((750, 750), RESIZABLE)

surface = pygame.display.get_surface()
if surface == None: 
    raise ValueError("No surface found")

fps = pygame.time.Clock()

maze = GridMaze(Size(75, 75))
ui = GridMazeUI(maze)
generator = DepthFirstGenerator(maze, GridIndex(0, 0))

GEN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(GEN_EVENT, 1)

loop = False
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == GEN_EVENT and loop:
            generator.perform_one_step()
            ui = GridMazeUI(maze)
    
    if pygame.key.get_pressed()[K_SPACE]:
        loop = True

    surface.fill(BLACK) #clears up the surface
    ui.draw_to(surface)

    pygame.display.update()
    fps.tick(60)