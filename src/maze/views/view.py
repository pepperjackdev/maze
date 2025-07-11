from pygame.surface import Surface

class View:
    def __init__(self, 
                 size: tuple[int, int], 
                 center: tuple[int, int]) -> None:
        self._surface = Surface(size)
        self._center = center
        self._children: set['View'] = set()

    def _set_size(self, size: tuple[int, int]):
        self._surface = Surface(size) # Surface's size is immutable

    def _set_center(self, center: tuple[int, int]):
        self._center = center

    def get_children(self) -> set['View']:
        return self._children

    def draw(self, 
             target: Surface, 
             center: tuple[int, int] | None = None, 
             size: tuple[int, int] | None = None):
        if center is not None: self._set_center(center)
        if size is not None: self._set_size(size)
        self._draw_children_to_surface()
        target.blit(self._surface, self._surface.get_rect(center=self._center))

    def _draw_children_to_surface(self):
        for child in self._children:
            child.draw(self._surface)