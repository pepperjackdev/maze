import pygame

from pygame.surface import Surface
from core import Size, OrtogonalMaze

from locals import *
from maze.core.utils import Point

class UI:
    def __init__(self) -> None:
        self.__surface: Surface | None = None

    def draw_to(self, target: Surface):
        self.__update_surface(target.get_size())
        assert self.__surface != None # as __update_surface(...) was called
        target.blit(self.__surface, (0, 0), self.__surface.get_rect())

    def __update_surface(self, size: tuple[int, int]):
        self.__provide_surface_of_size(size)
        self.__draw_to_surface()

    def __provide_surface_of_size(self, size: tuple[int, int]):
        if self.__surface == None or self.__surface.get_size() != size:
            self.__surface = Surface(size)

    def __draw_to_surface(self):
        raise NotImplementedError()

class OrtogonalMazeUI(UI):
    def __init__(self, maze: OrtogonalMaze) -> None:
        super().__init__()
        self.__maze = maze

    def __get_node_size_on_screen(self) -> Size:
        assert self.__surface != None
        return Size(
            self.__surface.get_height() // self.__maze.get_rows(),
            self.__surface.get_width() // self.__maze.get_columns()
        )

    def __draw_to_surface(self):
        self.__draw_walls_to_surface()

    def __draw_walls_to_surface(self):
        self.__draw_horizontal_walls_to_surface()
        self.__draw_vertical_walls_to_surface()

    def __get_point_on_surface_of(self, point: Point) -> Point:
        node_size_on_screen = self.__get_node_size_on_screen()
        return Point(
            point.row * node_size_on_screen.height,
            point.column * node_size_on_screen.width
        )

    def __draw_vertical_walls_to_surface(self):
        for row in range(self.__maze.get_rows()):
            for col in range(1, self.__maze.get_columns()):
                leftmost_cell_point, righmost_cell_point = Point(row, col - 1), Point(row, col)
                if self.__maze.there_is_wall(leftmost_cell_point, righmost_cell_point):
                    assert self.__surface != None # as this function gets called after __provide_surface_of_size(...)
                    pygame.draw.line(
                        self.__surface, 
                        BLACK,
                        self.__get_point_on_surface_of(Point(row, col)).as_tuple(),
                        self.__get_point_on_surface_of(Point(row + 1, col)).as_tuple(),
                        2
                    )

    def __draw_horizontal_walls_to_surface(self):
        for col in range(self.__maze.get_columns()):
            for row in range(1, self.__maze.get_rows()):
                uppermost_cell_point, downmost_cell_point = Point(row - 1, col), Point(row, col)
                if self.__maze.there_is_wall(uppermost_cell_point, downmost_cell_point):
                    assert self.__surface != None # as this function gets called after __provide_surface_of_size(...)
                    pygame.draw.line(
                        self.__surface,
                        BLACK,
                        self.__get_point_on_surface_of(Point(row, col)).as_tuple(),
                        self.__get_point_on_surface_of(Point(row, col + 1)).as_tuple()
                    )