from pygame.surface import Surface
from pygame.rect import Rect

class View:
    def __init__(self, 
                 size: tuple[int, int], 
                 center: tuple[int, int]) -> None:
        self._surface = Surface(size)
        self._center = center

    def _set_size(self, size: tuple[int, int]):
        self._surface = Surface(size)

    def _set_center(self, center: tuple[int, int]):
        self._center = center

    def draw(self, 
             target: Surface, 
             center: tuple[int, int] | None, 
             size: tuple[int, int] | None):
        if center is not None: self._set_center(center)
        if size is not None: self._set_size(size)
        target.blit(self._surface, self._surface.get_rect(center=self._center))