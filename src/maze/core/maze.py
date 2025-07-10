from . import Cell, Edge

Size = tuple[int, int]
Point = tuple[int, int]

class Maze:
    def __init__(self, size: Size) -> None:
        self._rows, self._cols = size
        self._cells = [[Cell() for _ in range(self._rows)] for _ in range(self._cols)]
        self._edges: set[Edge] = set()

    def size(self) -> Size:
        return self.rows(), self.cols()

    def rows(self) -> int:
        return self._rows

    def cols(self) -> int:
        return self._cols

    def cell(self, pos: Point) -> Cell:
        row, col = pos
        return self._cells[row][col]
    
    def link(self, cell_a, cell_b):
        self._edges.add(Edge(cell_a, cell_b))

    def unlink(self, cell_a, cell_b):
        self._edges.discard(Edge(cell_a, cell_b))