from enum import Enum
from typing import Any,Optional,  Dict, List
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin/'
from graphviz import Digraph as Graphviz


class EdgeType(Enum):
    directed = 1
    undirected = 2

class Vertex:
    data: Any
    index: int

    def __init__(self, data, index):
        self.data = data
        self.index = index

    def __repr__(self):
        return f'{self.data}:v{self.index}'


class Edge:
    source: Vertex
    destination: Vertex
    weight: float

    def __init__(self, s, d, w):
        self.source = s
        self.destination = d
        self.weight = w

    def __repr__(self):
        return f'{self.destination}'


class Graph:
    adjacencies: Dict[Vertex, List[Edge]]

    def __init__(self):
        self.adjacencies = dict()

    def create_vertex(self, data: Any):
        self.adjacencies[Vertex(data, len(self.adjacencies))] = list()

    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: float = None):
        graf.adjacencies[source].append(Edge(source, destination, weight))

    def add_undirected_edge(self, source: Vertex, destination: Vertex, weight: float = None):
        graf.adjacencies[source].append(Edge(source, destination, weight))
        graf.adjacencies[destination].append(Edge(destination, source, weight))

    def add(self, edge: EdgeType, source: Vertex, destination: Vertex, weight: float = None):
        if edge.name == "directed":
            self.add_directed_edge(source, destination, weight)
        else:
            self.add_undirected_edge(source, destination, weight)

    def show(self, name: Optional = "graf"):
        graff = Graphviz(comment='graf')
        visited = []
        for x in self.adjacencies.keys():
            self._show_helper(x, graff , visited)
        graff .render(f'output/{name}', view=True, format="png", quiet_view=False)
    def _show_helper(self, Vertex, graff , visited: List):
        if Vertex in visited:
            True
        else:
            graff .node(str(Vertex.index), str(Vertex.data))
            visited.append(Vertex)
            for neighbour in self.adjacencies[Vertex]:
                desc = ""
                if neighbour.weight != None:
                    desc += f"{neighbour.weight}"
                graff.edge(str(neighbour.source.index), str(neighbour.destination.index), label=desc)
                if not (neighbour.destination in visited):
                    self._show_helper(neighbour.destination, graff, visited)

    def __repr__(self):
        stirng = ""
        for data in self.adjacencies:
            stirng += f'- {data} ---->{self.adjacencies[data]}\n'
        return stirng


class GraphPath:
    tablica_kosztow: Dict[Vertex, int]
    tablica_parents: Dict[Vertex, List[Vertex]]
    visited: List[Vertex]
    path: List[Vertex]

    def __init__(self, g: Graph, p: Vertex, k: Vertex):
        self.tablica_kosztow = dict()
        self.tablica_parents = dict()
        self.visited = list()
        self.path = list()
        for child in g.adjacencies.keys():
            self.tablica_kosztow[child] = 900000
            self.tablica_parents[child] = None
        for neighbour in g.adjacencies[p]:
            self.tablica_kosztow[neighbour.destination] = neighbour.weight
            self.tablica_parents[neighbour.destination] = neighbour.source
        self.all_weighted_shortest_paths(g, p, k)
        print(f"Koszt najkrotszej trasy wynosi: {self.tablica_kosztow[k]}")

    def _dijkstra(self, g: Graph, Vertex_first: Vertex, Vertex_last: Vertex):
        self.visited.append(Vertex_first)
        v = min(self.tablica_kosztow, key=self.tablica_kosztow.get)
        while v != None:
            c = self.tablica_kosztow[v]
            self.visited.append(v)
            for edge in g.adjacencies[v]:
                nc = c + edge.weight
                if self.tablica_kosztow[edge.destination] > nc:
                    self.tablica_kosztow[edge.destination] = nc
                    self.tablica_parents[edge.destination] = v
            koszty_copy = self.tablica_kosztow.copy()
            v = min(koszty_copy, key=koszty_copy.get)
            while min(koszty_copy, key=koszty_copy.get) in self.visited:
                koszty_copy.pop(min(koszty_copy, key=koszty_copy.get))
                if len(koszty_copy.keys()) == 0:
                    v = None
                    break
                v = min(koszty_copy, key=koszty_copy.get)
        while Vertex_last is not None:
            self.path.append(Vertex_last)
            Vertex_last = self.tablica_parents[Vertex_last]
        self.path.reverse()

    def all_weighted_shortest_paths(self, g: Graph,Vertex_first: Vertex, Vertex_last: Vertex):
        li = [y for x in g.adjacencies.values() for y in x]
        if li[0].weight != None:
            self._dijkstra(g, Vertex_first, Vertex_last)
        print(self.path)


graf= Graph()

# GRAF 1
# graf.create_vertex(0)
# graf.create_vertex(1)
# graf.create_vertex(2)
# graf.create_vertex(3)
# lista_kluczy = [x for x in graf.adjacencies.keys()]
# graf.add(EdgeType(1), lista_kluczy[0], lista_kluczy[1], 4)
# graf.add(EdgeType(1), lista_kluczy[0], lista_kluczy[2], 3)
# graf.add(EdgeType(1), lista_kluczy[1], lista_kluczy[3], 2)
# graf.add(EdgeType(1), lista_kluczy[2], lista_kluczy[3], 7)
# graf.show()
# print(graf)
# gp = GraphPath(graf, lista_kluczy[0], lista_kluczy[3])

# GRAF 2
graf.create_vertex(0)
graf.create_vertex(1)
graf.create_vertex(2)
graf.create_vertex(3)
lista_kluczy = [x for x in graf.adjacencies.keys()]
graf.add(EdgeType(1), lista_kluczy[0], lista_kluczy[1], 8)
graf.add(EdgeType(1), lista_kluczy[1], lista_kluczy[2], 6)
graf.add(EdgeType(1), lista_kluczy[1], lista_kluczy[3], 5)
graf.add(EdgeType(1), lista_kluczy[2], lista_kluczy[3], 4)
graf.show()
# print(graf)
gp = GraphPath(graf, lista_kluczy[0], lista_kluczy[3])
#
# # GRAF 3
# graf.create_vertex(0)
# graf.create_vertex(1)
# graf.create_vertex(2)
# graf.create_vertex(3)
# lista_kluczy = [x for x in graf.adjacencies.keys()]
# graf.add(EdgeType(1), lista_kluczy[1], lista_kluczy[2], 9)
# graf.add(EdgeType(1), lista_kluczy[2], lista_kluczy[3], 1)
# graf.add(EdgeType(1), lista_kluczy[2], lista_kluczy[4], 5)
# graf.add(EdgeType(1), lista_kluczy[4], lista_kluczy[5], 10)
# graf.show()
# # print(graf)
# gp = GraphPath(graf, lista_kluczy[1], lista_kluczy[4])