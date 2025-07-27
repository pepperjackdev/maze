from pygame.surface import Surface

from abc import ABC, abstractmethod

IntPair = tuple[int, int]

class UI(ABC):
    def __init__(self) -> None:
        self.__surface: Surface | None = None
        self.__children: list[UI] = list()

    def append_children(self, *children: 'UI') -> None:
        self.__children.append(*children)

    def get_children(self) -> list['UI']:
        return self.__children
        
    def remove_children(self, *children: 'UI') -> None:
        for child in children:
            self.__children.remove(child)

    def blit_to_surface(self, target: Surface, point: IntPair = (0, 0)) -> None:
        self.__update_surface(target.get_size())

    def __update_surface(self, size: IntPair):
        self.__provide_surface_of_size(size)
        self.__blit_children_to_surface()
        self.__blit_to_surface()

    def __provide_surface_of_size(self, size: tuple[int, int]) -> None:
        if self._surface == None or self._surface.get_size() != size:
            self._surface = Surface(size)
    
    def __blit_children_to_surface(self):
        for child in self.__children:
            # as __provide_surface_of_size(size) 
            # has been called before
            assert self.__surface != None
            child.blit_to_surface(self.__surface)

    @abstractmethod
    def __blit_to_surface(self): ...

class MazeUI(UI):
    def __init__(self) -> None:
        super().__init__()
        # TODO: continue from here...