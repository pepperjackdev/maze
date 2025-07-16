import pygame
import sys
import asyncio

from pygame.locals import * #type: ignore

from mazecore import Maze, Cell, Status
from mazeui import MazeUI

pygame.init()

pygame.display.set_caption("Maze")
pygame.display.set_mode((600, 600), RESIZABLE)

surface = pygame.display.get_surface()
if surface == None: raise ValueError("No surface found")

fps = pygame.time.Clock()

maze = Maze((30, 30))
ui = MazeUI((600, 600), maze)

# Adding walls
def wallify(maze: Maze):
    for row in maze.cells:
        for cell in row:
            for neigh in cell.neighbours():
                maze.add_wall(cell, neigh)

wallify(maze)

# Maze generation
def generate(cell: Cell):
    cell.mark(Status.VISITED)
    for neighbour in cell.neighbours():
        if neighbour.status != Status.UNVISITED: continue
        maze.rem_wall(cell, neighbour)
        generate(neighbour)

generate(maze.get_cell((0, 0)))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    ui.draw(surface)

    pygame.display.update()
    fps.tick(60)
