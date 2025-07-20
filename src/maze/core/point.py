from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    @staticmethod
    def from_tuple(point: tuple[int, int]):
        row, column = point
        return Point(row, column)
    
    @staticmethod
    def to_tuple(point: 'Point'):
        return (point.row, point.column)

    row: int
    column: int

    def __add__(self, other: 'Point') -> 'Point':
        return Point(self.row + other.row, self.column + other.column)
