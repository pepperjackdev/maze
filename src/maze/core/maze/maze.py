from core.graph import Graph, Node

from abc import ABC, abstractmethod
from typing import TypeVar, Generic
from pyxtension.streams import stream

class Index(ABC):
    @abstractmethod
    def get_adjacent_indexes(self) -> set['Index']:
        pass

I = TypeVar("I", bound="Index")

class Bound(ABC, Generic[I]):
    @abstractmethod
    def get_first_index(self) -> I: ...

    @abstractmethod
    def get_last_index(self) -> I: ...

    @abstractmethod
    def is_index_in_bound(self, index: I) -> bool: ...

    def is_index_out_bound(self, index: I) -> bool: 
        return not self.is_index_in_bound(index)

B = TypeVar("B", bound=Bound)

class Maze(ABC, Generic[I, B]):
    def __init__(self, bound: B) -> None:
        self._bound: B = bound
        self._graph: Graph = Graph()
        self._map: dict[I, Node] = dict()
        self._init_map_and_graph()

    @abstractmethod
    def _init_map_and_graph(self): ...

    def get_bound(self) -> B:
        return self._bound 
 
    def get_node(self, index: I) -> Node:
        if self.get_bound().is_index_out_bound(index):
            raise ValueError(f"There isn't a Node at {index}")
        return self._map[index]
    
    def get_optional_node(self, index: I) -> Node | None:
            return self._map.get(index, None)

    def get_indexes_adjacent_to(self, index: I) -> set[I]:
        return stream(index.get_adjacent_indexes()).filter(
            lambda idx: self.get_bound().is_index_in_bound(idx)
        ).to_set()

    def get_indexes_adjacent_and_linked_to(self, index: I) -> set:
         return stream(self.get_indexes_adjacent_to(index)).filter(
              lambda idx: not self.there_is_wall(index, idx)
         ).to_set()
    
    def add_wall(self, index_a: I, index_b: I):
        self._graph.unlink(
            self.get_node(index_a), 
            self.get_node(index_b)
        )
    
    def remove_wall(self, index_a: I, index_b: I):
        self._graph.link(
            self.get_node(index_a), 
            self.get_node(index_b)
        )

    def there_is_wall(self, index_a: I, index_b: I):
        return not self._graph.linked(
            self.get_node(index_a), 
            self.get_node(index_b)
        )
