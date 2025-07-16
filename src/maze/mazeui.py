import pygame
from mazecore import Maze, Cell, Status

from locals import *

class MazeUI:
    def __init__(self, size: tuple[int, int], maze: Maze) -> None:
        self._surface = pygame.surface.Surface(size)
        self._maze = maze

    def _cell_length(self):
        return self._surface.get_width() // self._maze.rows

    def get_pos_of(self, cell: Cell):
        if (pos := self._maze.get_pos_of(cell)) != None:
            row, col = pos
            return row * self._cell_length(), col * self._cell_length()
        raise ValueError()

    def draw(self, surface: pygame.surface.Surface):
        self._surface.fill(WHITE)
        self._draw_cells()
        self._draw_walls()
        surface.blit(self._surface, (0, 0), self._surface.get_rect())
        
    def _draw_walls(self):
        for wall in self._maze.get_walls():
            it = iter(wall.cells)
            cell_a_r, cell_a_c = self.get_pos_of(next(it))
            cell_b_r, cell_b_c = self.get_pos_of(next(it))
            if cell_a_r == cell_b_r:
                wall_start = (max(cell_a_c, cell_b_c), cell_a_r)
                wall_end = (max(cell_a_c, cell_b_c), cell_a_r + self._cell_length())
                pygame.draw.line(self._surface, BLACK, wall_start, wall_end, 2)
            if cell_a_c == cell_b_c:
                wall_start = (cell_a_c, max(cell_a_r, cell_b_r))
                wall_end = (cell_a_c + self._cell_length(), max(cell_a_r, cell_b_r))
                pygame.draw.line(self._surface, BLACK, wall_start, wall_end, 2)

    def _draw_cells(self):
        for row in range(self._maze.rows):
            for col in range(self._maze.cols):
                cell = self._maze.get_cell((row, col))
                assert cell != None
                starty, startx = self.get_pos_of(cell)
                self._surface.fill(BLUE if cell.status == Status.UNVISITED else WHITE, pygame.Rect(startx, starty, self._cell_length(), self._cell_length()))
                