import pygame

from pygame.surface import Surface
from core import Point, OrtogonalMaze

from locals import *

class UI:
    def __init__(self) -> None:
        self.__surface: Surface | None = None

    def draw_to(self, target: Surface):
        self.__update_surface(target.get_size())
        assert self.__surface != None # as __update_surface(...) was called
        target.blit(self.__surface, (0, 0), self.__surface.get_rect())

    def __update_surface(self, size: tuple[int, int]):
        self.__update_surface_size(size)
        self.__draw_to_surface()

    def __update_surface_size(self, size: tuple[int, int]):
        if self.__surface == None or self.__surface.get_size() != size:
            self.__surface = Surface(size)

    def __draw_to_surface(self):
        raise NotImplementedError()

class OrtogonalMazeUI(UI):
    def __init__(self, maze: OrtogonalMaze) -> None:
        super().__init__()
        self.__maze = maze

    def __draw_to_surface(self):
        self.__draw_walls_to_surface()

    def __draw_walls_to_surface(self):
        self.__draw_horizontal_walls_to_surface()
        self.__draw__vertical_walls_to_surface()

    def __draw_horizontal_walls_to_surface(self):
        for row in range(self.__maze.get_rows()):
            for col in range(1, self.__maze.get_columns()):
                cell_a_point, cell_b_point = Point(row, col - 1), Point(row, col)
                if self.__maze.there_is_wall(cell_a_point, cell_b_point):
                    # TODO: continue from here...
                    #   1. Evaluate position on surface of a cell
                    #   2. Finish this function
                    #   3. Implement the next one
                    #   4. Erase old implementation of maze and put this one
                    #   5. Expant with new features
                    """
                    pygame.draw.line(
                        self.__surface, 
                        BLACK, 
                    )
                    """
    
    def __draw__vertical_walls_to_surface(self):
        ...