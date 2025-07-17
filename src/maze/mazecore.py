from enum import Enum

Size = tuple[int, int] 
Point = tuple[int, int]

def translate(start: Point, delta: Point):
    start_row, start_column = start
    delta_row, delta_column = delta
    return start_row + delta_row, start_column + delta_column

class Status(Enum):
    UNVISITED = 0
    VISITED = 1

class Cell:
    def __init__(self, position: Point) -> None:
        self._status = Status.UNVISITED
        self._position = position

    def get_status(self):
        return self._status

    def set_status(self, status: Status):
        self._status = status

    def get_position(self):
        return self._position

class Wall:
    def __init__(self, cell_a, cell_b) -> None:
        self._cells = frozenset([cell_a, cell_b])

    def __eq__(self, value: object) -> bool:
        if isinstance(value, Wall):
            return self._cells == value._cells
        return False
    
    def __hash__(self) -> int:
        return hash(self._cells)

class Maze:
    _NEIGHBOURS_DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def __init__(self, size: Size) -> None:
        self._rows, self._columns = size
        self._cells = [[Cell((row, column)) for row in range(self._rows)] for column in range(self._columns)]
        self._walls = set()

    def get_rows(self):
        return self._rows
    
    def get_columns(self):
        return self._columns
    
    def get_size(self):
        return self._rows, self._columns
    
    def _is_valid_position(self, position: Point) -> bool:
        row, column = position
        return 0 <= row < self._rows and 0 <= column < self._columns
    
    def get_cells(self) -> list[list[Cell]]:
        return self._cells

    def get_cell(self, position) -> Cell | None:
        if self._is_valid_position(position): 
            row, column = position
            return self._cells[row][column]
        return None
    
    def get_cells_adjacent_to(self, cell: Cell) -> set[Cell]:
        neighbours = set()
        for direction in Maze._NEIGHBOURS_DIRECTIONS:
            neighbour = self.get_cell(translate(cell.get_position(), direction))
            if neighbour != None:
                neighbours.add(neighbour)
        return neighbours
    
    def get_walls(self) -> set[Wall]:
        return self._walls
    
    def get_wall(self, wall: Wall):
        return wall in self._walls
    
    def add_wall(self, wall: Wall):
        self._walls.add(wall)

    def remove_wall(self, wall: Wall):
        self._walls.discard(wall)
