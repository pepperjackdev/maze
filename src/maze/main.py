import pygame
import sys
import asyncio

from pygame.locals import * #type: ignore

from mazecore import Maze, Cell, Wall, Status
from mazeui import MazeUI

pygame.init()

pygame.display.set_caption("Maze")
pygame.display.set_mode((600, 600), RESIZABLE)

surface = pygame.display.get_surface()
if surface == None: raise ValueError("No surface found")

fps = pygame.time.Clock()

maze = Maze((30, 30))
ui = MazeUI((600, 600), maze)

def add_all_walls(maze: Maze):
    cell = maze.get_cell((0, 0))
    cell.set_status(Status.VISITED)
    for neighbour in maze.get_cells_adjacent_to(cell):
        if neighbour.get_status() == Status.UNVISITED:
            maze.add_wall(Wall(cell, neighbour))
            depth_first(neighbour)

def depth_first(cell: Cell):
    cell.set_status(Status.VISITED)
    for neighbour in maze.get_cells_adjacent_to(cell):
        if neighbour.get_status() == Status.UNVISITED:
            maze.remove_wall(Wall(cell, neighbour))
            depth_first(neighbour)

add_all_walls(maze)
# depth_first(maze.get_cell((0, 0)))
print(maze.get_wall(Wall(maze.get_cell((3, 0)), maze.get_cell((4, 0)))))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    ui.draw_to(surface)

    pygame.display.update()
    fps.tick(60)
