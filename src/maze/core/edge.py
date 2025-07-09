from . import Cell

class Edge:
    def __init__(self, cell_a: Cell, cell_b: Cell) -> None:
        self._cell_a = cell_a
        self._cell_b = cell_b

    def __eq__(self, obj: object) -> bool:
        if not isinstance(obj, Edge): return False
        return self.cell_a() == obj.cell_a() and self.cell_b() == obj.cell_b()

    def cells(self):
        return self.cell_a(), self.cell_b()

    def cell_a(self):
        return self._cell_a
    
    def cell_b(self):
        return self._cell_b
