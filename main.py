import graf_mst

class Node:
    def __init__(self, key_, value_=None):
        self.key = key_
        self.value = value_

    def get_value(self):
        return self.value

    def set_value(self, value_):
        self.value = value_

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return hash(self.key)

    def __str__(self):
        return self.key


class NeighbourList:
    def __init__(self):
        self.graph = {}

    def is_empty(self):
        return self.graph == {}

    def insert_vertex(self, vertex):
        if vertex not in self.graph.keys():
            self.graph[vertex] = {}

    def insert_edge(self, vertex1, vertex2, edge=None):
        if vertex2 not in self.graph.keys():
            self.graph[vertex2] = {}
        self.graph[vertex1][vertex2] = edge
        self.graph[vertex2][vertex1] = edge

    def delete_edge(self, vertex1, vertex2):
        self.graph[vertex1].pop(vertex2)
        self.graph[vertex2].pop(vertex1)

    def delete_vertex(self, vertex):
        self.graph.pop(vertex)

        for key in self.graph:
            for key2 in self.graph[key]:
                i = None
                if key2 == vertex:
                    i = key2
                    self.graph[key].pop(i)
                    break

    def get_vertex(self,vertex_id):
        return vertex_id

    def vertices(self):
        return [k for k in self.graph]

    def neighbours(self, vertex_id):
        wynik = []
        for nghbr, edge in self.graph[vertex_id].items():
            wynik.append((nghbr, edge))
        return wynik


def Prim(graf, letter):
    intree = {}
    parent = {}
    distance = {}

    for node in graf.graph.keys():
        intree[node] = 0
        parent[node] = None
        distance[node] = float('inf')

    v = Node(letter)
    new_graf = NeighbourList()
    new_graf.insert_vertex(v)

    edge_sum = 0

    while intree[v] == 0:
        intree[v] = 1

        neighbours = graf.neighbours(v)

        for n,e in neighbours:
            edge = graf.graph[v][n]
            if intree[n] == 0 and edge < distance[n]:
                distance[n] = edge
                parent[n] = v

        min_edge = float('inf')
        min_u = None
        for u in graf.graph.keys():
            if u not in new_graf.graph.keys():
                if distance[u] < min_edge:
                    min_edge = distance[u]
                    min_u = u

        if min_u is not None:
            new_graf.insert_edge(parent[min_u], min_u, min_edge)
            edge_sum += min_edge
            v = min_u

    return new_graf, edge_sum


def printGraph(g):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end = " -> ")
        for (n, w) in g.neighbours(v):
            print(n, w, end=";")
        print()
    print("-------------------")


G = NeighbourList()

for tuple in graf_mst.graf:
    ver1 = Node(tuple[0])
    ver2 = Node(tuple[1])
    G.insert_vertex(ver1)
    G.insert_edge(ver1,ver2,tuple[2])

new_G, edge_sum = Prim(G, 'A')

printGraph(new_G)

# suma krawedzi: 38


