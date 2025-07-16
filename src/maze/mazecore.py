from enum import Enum

Size = tuple[int, int] 
Point = tuple[int, int]

def translate(source: Point, vector: Point):
    sy, sx, vy, vx = source + vector
    return sy + vy, sx + vx

NEIGHBOUR_DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

class Status(Enum):
    UNVISITED = 0
    VISITED = 1

class Cell:
    def __init__(self, maze: 'Maze') -> None:
        self.maze = maze
        self.status = Status.UNVISITED

    def neighbours(self) -> set['Cell']:
        neighbours = set()
        for direction in NEIGHBOUR_DIRECTIONS:
            cell = self.maze.get_cell(translate(self.maze.get_pos_of(self), direction))
            if cell != None:
                neighbours.add(cell)
        return neighbours

    def mark(self, status: Status):
        self.status = status

class Wall:
    def __init__(self, cell_a, cell_b) -> None:
        self.cells = frozenset([cell_a, cell_b])

    def __eq__(self, value: object) -> bool:
        if isinstance(value, Wall):
            return self.cells == value.cells
        return False
    
    def __hash__(self) -> int:
        return hash(self.cells)

class Maze:
    def __init__(self, size: Size) -> None:
        self.rows, self.cols = size
        self.cells = [[Cell(self) for _ in range(self.rows)] for _ in range(self.cols)]
        self.walls = set()
    
    def get_size(self):
        return self.rows, self.cols
    
    def get_cell(self, pos) -> Cell | None:
        row, col = pos
        if not 0 <= row < self.rows or not 0 <= col < self.cols: return None
        return self.cells[row][col]
    
    def get_pos_of(self, cell: Cell) -> Point | None:
        for row in range(self.rows):
            for col in range(self.cols):
                if cell == self.get_cell((row, col)):
                    return (row, col)
        return None
    
    def get_walls(self) -> set[Wall]:
        return self.walls
    
    def add_wall(self, cell_a: Cell, cell_b: Cell):
        self.walls.add(Wall(cell_a, cell_b))

    def is_linked(self, cell_a: Cell, cell_b: Cell):
        return not Wall(cell_a, cell_b) in self.walls

    def rem_wall(self, cell_a: Cell, cell_b: Cell):
        self.walls.discard(Wall(cell_a, cell_b))