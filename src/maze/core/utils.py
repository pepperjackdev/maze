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