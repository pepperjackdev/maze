from core.graph import Node
from core.maze import Index, Bound, Maze

from pyxtension.streams import stream
from dataclasses import dataclass

IntPair = tuple[int, int]

@dataclass(frozen=True)
class GridIndex(Index):
    __ADJACENT_RELATIVE_INDEXES = [
        (1, 0),     # up
        (-1, 0),    # down
        (0, 1),     # right
        (0, -1)     # left
    ]

    row: int
    column: int

    def get_adjacent_indexes(self) -> set[Index]: 
        return stream(self.__ADJACENT_RELATIVE_INDEXES).map(
            lambda relative: self + relative
        ).to_set()

    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, GridIndex): 
            return self.row == obj.row and self.column == obj.column
        return False
    
    def __add__(self, other: 'GridIndex' | IntPair) -> 'GridIndex':
        if isinstance(other, GridIndex): 
            return GridIndex(self.row + other.row, self.column + other.column)
        else: 
            return GridIndex(self.row + other[0], self.column + other[1])

class GridBound(Bound):
    def __init__(self, rows: int, cols: int) -> None:
        self.__rows = rows
        self.__cols = cols

    def get_rows(self) -> int:
        return self.__rows
    
    def get_cols(self) -> int:
        return self.__cols
    
    def get_first_index(self) -> GridIndex:
        return GridIndex(0, 0)
    
    def get_last_index(self) -> GridIndex:
        return GridIndex(
            self.__rows - 1, 
            self.__cols - 1
        )

    def is_index_in_bound(self, index: GridIndex) -> bool:
        return (0 <= index.column < self.get_rows() and
                0 <= index.row < self.get_cols())

class GridMaze(Maze[GridIndex, GridBound]):
    def __init__(self, bound: GridBound) -> None:
        super().__init__(bound)

    def _init_map_and_graph(self):
        for row in range(self._bound.get_rows()):
            for column in range(self._bound.get_cols()):
                node = Node()
                self._map[GridIndex(row, column)] = node
                self._graph.add(node)
