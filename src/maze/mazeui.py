import pygame
from .maze import Maze

class MazeUI:
    def __init__(self, size: tuple[int, int], maze: Maze) -> None:
        self._surface = pygame.surface.Surface(size)
        self._maze = maze

    