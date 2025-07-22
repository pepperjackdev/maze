from core import Graph, Node
from core.utils import Point, Size

from bidict import bidict

class Maze:
    def __init__(self, graph: Graph = Graph()) -> None:
        self._graph = graph
    
class OrtogonalMaze(Maze):
    __ADJACENT_NODES_DIRECTIONS = [
        Point(1, 0),    # up
        Point(-1, 0),   # down
        Point(0, 1),    # left
        Point(0, -1)    # right
    ]

    def __init__(self, size: Size) -> None:
        super().__init__()
        self.__size = size
        self.__map = bidict()
        self.__init_map_and_graph()

    def __init_map_and_graph(self):
        # to make more efficient the init of map and graph,
        # they are performed at the same time
        for row in range(self.__size.height):
            for column in range(self.__size.width):
                node = Node()
                self.__map[Point(row, column)] = node
                self._graph.add(node)

    def get_rows(self):
        return self.__size.height
    
    def get_columns(self):
        return self.__size.width
    
    def get_size(self):
        return self.__size
    
    def __validate(self, point: Point) -> bool:
        return 0 <= point.row < self.get_rows() and 0 <= point.column < self.get_columns()
    
    def get_node(self, point: Point) -> Node | None:
        #FIXME: point seems to not be in self.__map() even if it is!
        if self.__validate(point):
            return self.__map[point]
        return None

    def get_node_else_raise(self, point: Point):
        if (node := self.get_node(point)) != None:
            return node
        raise ValueError()
    
    def get_nodes_adjacent_to(self, node: Node):
        adjacent_nodes = set()
        for direction in OrtogonalMaze.__ADJACENT_NODES_DIRECTIONS:
            adjacent = self.get_node(self.__map.inverse[node] + direction)
            if adjacent != None: adjacent_nodes.add(adjacent)
        return adjacent_nodes
    
    def get_nodes_adjacent_and_linked_to(self, node: Node):
        return set.intersection(
            self.get_nodes_adjacent_to(node),
            self._graph.neighbours_of(node)
        )
    
    def add_wall(self, node_a: Point, node_b: Point):
        self._graph.unlink(
            self.get_node_else_raise(node_a), 
            self.get_node_else_raise(node_b)
        )
    
    def remove_wall(self, node_a: Point, node_b: Point):
        self._graph.link(
            self.get_node_else_raise(node_a), 
            self.get_node_else_raise(node_b)
        )

    def there_is_wall(self, node_a: Point, node_b: Point):
        self._graph.linked(
            self.get_node_else_raise(node_a), 
            self.get_node_else_raise(node_b)
        )