from core.graph import Node
from core.maze import Maze, Index

from core.utils import Size

from dataclasses import dataclass

@dataclass(frozen=True)
class GridIndex(Index):
    @staticmethod
    def from_tuple(point: tuple[int, int]):
        row, column = point
        return GridIndex(row, column)

    @staticmethod
    def to_tuple(point: 'GridIndex'):
        return (point.row, point.column)

    row: int
    column: int

    def __add__(self, other: 'GridIndex') -> 'GridIndex':
        return GridIndex(self.row + other.row, self.column + other.column)
    
    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, GridIndex):
            return self.row == obj.row and self.column == obj.column
        return False

    def reversed(self):
        return GridIndex(self.column, self.row)

    def as_tuple(self):
        return GridIndex.to_tuple(self)

class GridMaze(Maze):
    __ADJACENT_NODES_DIRECTIONS = [
        GridIndex(1, 0),    # up
        GridIndex(-1, 0),   # down
        GridIndex(0, 1),    # right
        GridIndex(0, -1)    # left
    ]

    def __init__(self, size: Size) -> None:
        self.__size = size
        super().__init__()

    def _init_map_and_graph(self):
        for row in range(self.get_rows()):
            for column in range(self.get_columns()):
                node = Node()
                self._map[GridIndex(row, column)] = node
                self._graph.add(node)

    def get_rows(self):
        return self.__size.height
    
    def get_columns(self):
        return self.__size.width
    
    def get_size(self):
        return self.__size
    
    def get_indexes_adjacent_to(self, index: GridIndex):
        adjacent_indexes = set()
        for direction in GridMaze.__ADJACENT_NODES_DIRECTIONS:
            adjacent_node = self.get_node(index + direction)
            if adjacent_node != None: adjacent_indexes.add(index + direction)
        return adjacent_indexes

