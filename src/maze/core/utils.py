from dataclasses import dataclass

@dataclass(frozen=True)
class Size:
    @staticmethod
    def from_tuple(size: tuple[int, int]):
        height, width = size
        return Size(height, width)
    
    @staticmethod
    def to_tuple(size: 'Size'):
        return (size.height, size.width)

    height: int
    width: int

    def as_tuple(self):
        return Size.to_tuple(self)

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
    
    def swapped(self):
        return Point(self.column, self.row)

    def as_row_column_tuple(self):
        return Point.to_tuple(self)
    
    def as_column_row_tuple(self):
        return Point.to_tuple(self.swapped())

    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, Point):
            return self.row == obj.row and self.column == obj.column
        return False