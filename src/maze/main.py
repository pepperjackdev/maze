import pygame
import sys

from pygame.locals import RESIZABLE, QUIT

from mazecore import Maze, Cell, Wall, Status
from mazeui import MazeUI

sys.setrecursionlimit(10000) #FIXME: I'm dangerous!

pygame.init()

pygame.display.set_caption("Maze")
pygame.display.set_mode((600, 600), RESIZABLE)

surface = pygame.display.get_surface()
if surface == None: raise ValueError("No surface found")

fps = pygame.time.Clock()

maze = Maze((100, 100))
maze_ui = MazeUI((600, 600), maze)

# just fill with walls
for row in maze.get_cells():
    for cell in row:
        for neighbour in maze.get_cells_adjacent_to(cell):
            maze.add_wall(Wall(cell.get_position(), neighbour.get_position()))

# using depth-first to generate the maze
def depth_first(maze: Maze, cell: Cell):
    cell.set_status(Status.VISITED)
    for neighbour in maze.get_cells_adjacent_to(cell):
        if neighbour is not None and neighbour.get_status() == Status.UNVISITED:
            maze.remove_wall(Wall(cell.get_position(), neighbour.get_position()))
            depth_first(maze, neighbour)

depth_first(maze, maze.get_cell((0, 0)))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    maze_ui.draw_to(surface)

    pygame.display.update()
    fps.tick(60)
