class Graph:
    def __init__(self):
        self.adj_list = {}

    def all(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])

    def add(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def edge(self, vertex1, vertex2):
        if vertex1 and vertex2 not in self.adj_list.keys():
            return False
        self.adj_list[vertex1].append(vertex2)
        self.adj_list[vertex2].append(vertex1)
        return True
    
    def remove_edge(self, vertex1, vertex2):
        if vertex1 and vertex2 in self.adj_list.keys():
            try:
                self.adj_list[vertex1].remove(vertex2)
                self.adj_list[vertex2].remove(vertex1)
            except ValueError:
                pass
            return True
        return False
    
    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for v in self.adj_list[vertex]:
                self.adj_list[v].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False

graph = Graph()
graph.add('A')
graph.add('B')
graph.add('C')

graph.edge('A','B')
graph.edge('C','A')
graph.edge('C','B')

graph.remove_edge('A','A')
graph.remove_vertex('A')
graph.all()