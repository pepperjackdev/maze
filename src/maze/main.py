import pygame
import sys

from pygame.locals import RESIZABLE, QUIT

from mazecore import Maze, Cell, Wall, Status
from mazeui import MazeUI

pygame.init()

pygame.display.set_caption("Maze")
pygame.display.set_mode((600, 600), RESIZABLE)

surface = pygame.display.get_surface()
if surface == None: raise ValueError("No surface found")

fps = pygame.time.Clock()

maze = Maze((30, 30))
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

depth_first(maze, maze.get_cell((0, 0))) #type: ignore
maze.reset_visits()

def solving_depth_first(maze: Maze, current: Cell, target: Cell, iter = 0):
    current.set_status(Status.VISITED)
    if current.get_position() == target.get_position(): 
        return list([current])
    for neighbour in maze.get_linked_cells_adjacent_to(current):
        if neighbour.get_status() == Status.UNVISITED:
            if (result := solving_depth_first(maze, neighbour, target, iter + 1)) != []:
                result.append(current)
                return result
    return []
                
path = solving_depth_first(maze, maze.get_cell((0, 0)), maze.get_cell((29, 29)))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    maze_ui.draw_to(surface, path)

    pygame.display.update()
    fps.tick(60)
