from pygame.surface import Surface

from core import Maze
from . import View

from locals import *

class MazeView(View):
    def __init__(self, 
                 maze: Maze, 
                 size: tuple[int, int], 
                 center: tuple[int, int]) -> None:
        super().__init__(size, center)
        self._maze = maze

    def draw(self, 
             target: Surface, 
             center: tuple[int, int] | None = None, 
             size: tuple[int, int] | None = None):
        super().draw(target, center, size)
        self._surface.fill(BLUE)
