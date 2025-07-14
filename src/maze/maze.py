from enum import Enum

Size = tuple[int, int] 
Point = tuple[int, int]

class Direction(Enum):
    UP = 0
    LEFT = 1
    DOWN = 2
    RIGHT = 3

class Cell:
    def __init__(self, maze: 'Maze', coords: Point) -> None:
        self._maze = maze
        self._row, self._col = coords
    
    def neighbours(self) -> dict[Direction, 'Cell']:
        ...

class Maze:
    def __init__(self, size: Size) -> None:
        self._rows, self._cols = size
        self._cells: dict[Cell, list[Cell]] = dict()
        for row in range(self._rows):
            for col in range(self._cols):
                self._cells[Cell((row, col))] = list()
    
    def get_size(self):
        return self._rows, self._cols
    
    def add_wall(self, cell_a: Cell, cell_b: Cell):
        return 