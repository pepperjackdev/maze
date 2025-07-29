from core.maze import Maze, Index

from enum import Enum

class Status(Enum):
    UNVISITED = 0
    VISITED = 1

class Browser:
    def __init__(self, maze: Maze) -> None:
        self.__maze = maze
        self.__status_map = dict()

    def get_maze(self):
        return self.__maze