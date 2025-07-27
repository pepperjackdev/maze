from abc import ABC, abstractmethod
from enum import Enum
from core.maze import Maze, Index

class Generator(ABC):
    def __init__(self, maze: Maze) -> None:
        self._maze: Maze = maze

    @abstractmethod
    def perform_one_step(self) -> bool: ...

    def perform_all_steps(self) -> None:
        while self.perform_one_step(): pass

class Status(Enum):
    UNVISITED = 0
    VISITED = 1

class DepthFirstGenerator(Generator):
    def __init__(self, maze: Maze, start: Index) -> None:
        super().__init__(maze)
        self.__stack = list([start])
        self.__map = dict()

    def __get_status_of(self, index: Index) -> Status:
        return self.__map.get(index, Status.UNVISITED)
    
    def __set_status_of(self, index: Index, status: Status) -> None:
        self.__map[index] = status

    def __get_adjacent_unvisited_indexs(self, index: Index) -> set:
        unvisited_adjacent_index = set()
        for current in self._maze.get_indexes_adjacent_to(index):
            if self.__get_status_of(current) == Status.UNVISITED:
                unvisited_adjacent_index.add(current)
        return unvisited_adjacent_index

    def perform_one_step(self) -> bool:
        if len(self.__stack) > 0:
            index = self.__stack[-1]
            if len(self.__stack) > 1: 
                self._maze.remove_wall(index, self.__stack[-2])
            self.__set_status_of(index, Status.VISITED)
            if len(adjacent_unvisited_indexs := self.__get_adjacent_unvisited_indexs(index)) > 0:
                self.__stack.append(adjacent_unvisited_indexs.pop())
            else:
                self.__stack.pop()
            return True
        return False