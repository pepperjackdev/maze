from . import Cell, Edge

Size = tuple[int, int]

class Maze:
    def __init__(self, size: Size) -> None:
        self._rows, self._cols = size
        self._cells = [[Cell() for _ in range(self._rows)] for _ in range(self._cols)]
        self._edges: set[Edge] = set()

    def size(self):
        return self.rows(), self.cols()
    
    def rows(self):
        return self._rows
    
    def cols(self):
        return self._cols