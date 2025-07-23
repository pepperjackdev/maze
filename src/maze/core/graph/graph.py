
class Node:
    def __str__(self) -> str:
        return "Node()"
    
    def __repr__(self) -> str:
        return self.__str__()

class Edge:
    def __init__(self, node_a: Node, node_b: Node) -> None:
        self.__nodes = frozenset([node_a, node_b])

    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, Edge):
            return self.nodes() == obj.nodes()
        return False
    
    def __hash__(self) -> int:
        return hash(self.__nodes)

    def nodes(self) -> frozenset[Node]:
        return self.__nodes

class Graph:
    def __init__(self) -> None:
        self.__nodes = set()
        self.__edges = set()

    def nodes(self) -> frozenset[Node]:
        return frozenset(self.__nodes)

    def add(self, node: Node) -> None:
        self.__nodes.add(node)

    def remove(self, node: Node) -> None:
        self.__nodes.discard(node)

    def edges(self) -> frozenset[Edge]:
        return frozenset(self.__edges)

    def link(self, node_a: Node, node_b: Node) -> None:
        self.__edges.add(Edge(node_a, node_b))

    def unlink(self, node_a: Node, node_b: Node) -> None:
        self.__edges.discard(Edge(node_a, node_b))

    def linked(self, node_a: Node, node_b: Node) -> bool:
        return Edge(node_a, node_b) in self.__edges

    def neighbours_of(self, node) -> set[Node]:
        neighbours = set()
        for n in self.__nodes:
            if self.linked(n, node):
                neighbours.add(n)
        return neighbours