import pygame
from mazecore import Maze, Cell, Status

from locals import *

class MazeUI:
    def __init__(self, size: tuple[int, int], maze: Maze) -> None:
        self._surface = pygame.surface.Surface(size)
        self._maze = maze

    def _cell_length(self):
        return self._surface.get_width() // self._maze._rows

    def get_cell_position_on_screen(self, cell: Cell):
        row, column = cell.get_position()
        return row * self._cell_length(), column * self._cell_length()
        
    def draw_to(self, target: pygame.surface.Surface):
        self._draw_to_surface()
        target.blit(self._surface, (0, 0), self._surface.get_rect())

    def _draw_to_surface(self):
        self._clear_surface()
        self._draw_cells_to_surface()
        self._draw_walls_to_surface()

    def _clear_surface(self):
        self._surface.fill(WHITE)
        
    def _draw_walls_to_surface(self):
        for wall in self._maze.get_walls():
            iterator = iter(wall._cells)
            cell_a_y, cell_a_x = self.get_cell_position_on_screen(next(iterator))
            cell_b_y, cell_b_x = self.get_cell_position_on_screen(next(iterator))
            if cell_a_y == cell_b_y:
                wall_start = (max(cell_a_x, cell_b_x), cell_a_y)
                wall_end = (max(cell_a_x, cell_b_x), cell_a_y + self._cell_length())
                pygame.draw.line(self._surface, BLACK, wall_start, wall_end, 2)
            if cell_a_x == cell_b_x:
                wall_start = (cell_a_x, max(cell_a_y, cell_b_y))
                wall_end = (cell_a_x + self._cell_length(), max(cell_a_y, cell_b_y))
                pygame.draw.line(self._surface, BLACK, wall_start, wall_end, 2)

    def _draw_cells_to_surface(self):
        for row in range(self._maze._rows):
            for col in range(self._maze._columns):
                cell = self._maze.get_cell((row, col))
                assert cell != None
                starty, startx = self.get_cell_position_on_screen(cell)
                self._surface.fill(BLUE if cell._status == Status.UNVISITED else WHITE, pygame.Rect(startx, starty, self._cell_length(), self._cell_length()))
                