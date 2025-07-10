from pygame.surface import Surface

from core import Maze
from . import View

from locals import *

class MazeView(View):
    def __init__(self, surface: Surface, maze: Maze) -> None:
        super().__init__(surface)
        self._maze = maze