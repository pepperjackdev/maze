from core.graph import Graph, Node

from abc import ABC, abstractmethod
from typing import TypeVar, Generic

class Index: ...

I = TypeVar("I", bound="Index")

class Maze(ABC, Generic[I]):
    def __init__(self) -> None:
        self._graph = Graph()
        self._map = dict()
        self._init_map_and_graph()

    @abstractmethod
    def _init_map_and_graph(self): ...

    def get_node(self, index: I) -> Node | None:
            return self._map.get(index, None)
    
    def get_node_else_raise(self, index: I):
        if (node := self.get_node(index)) != None: 
            return node
        raise ValueError(f"There isn't a Node at {index}")
    
    @abstractmethod
    def get_indexes_adjacent_to(self, index: I) -> set: ...

    def get_nodes_adjacent_and_linked_to(self, index: I) -> set:
         return set.intersection(
              self.get_indexes_adjacent_to(index),
              self._graph.neighbours(self.get_node_else_raise(index))
         )
    
    def add_wall(self, index_a: I, index_b: I):
        self._graph.unlink(
            self.get_node_else_raise(index_a), 
            self.get_node_else_raise(index_b)
        )
    
    def remove_wall(self, index_a: I, index_b: I):
        self._graph.link(
            self.get_node_else_raise(index_a), 
            self.get_node_else_raise(index_b)
        )

    def there_is_wall(self, index_a: I, index_b: I):
        return not self._graph.linked(
            self.get_node_else_raise(index_a), 
            self.get_node_else_raise(index_b)
        )
