class Graph:
    def __init__(self, graph_dict={}):
        self.graph_dict = graph_dict

    def vertices(self):
        return list(self.graph_dict.keys())

    def edges(self):
        edges = []
        for vertex in self.graph_dict:
           for neighbor in self.graph_dict[vertex]:
               edges.append((vertex, neighbor))
        return edges

    def add_vertex(self, vertex):
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []

    def add_edge(self, edge):
        v_1, v_2 = edge
        if v_1 in self.graph_dict and v_2 not in self.graph_dict[v_1]:
            self.graph_dict[v_1].append(v_2)
        elif v_2 in self.graph_dict and v_1 not in self.graph_dict[v_2]:
            self.graph_dict[v_2].append(v_1)
        elif v_1 not in self.graph_dict:
            self.graph_dict[v_1] = [v_2]
        elif v_2 not in self.graph_dict:
            self.graph_dict[v_2] = [v_1]

    def __str__(self):
        res = "vertices: "
        for node in self.graph_dict:
            res += str(node) + ", "
        res += "\nedges: "
        for edge in self.edges():
            res += str(edge) + ", "
        return res 

if __name__ == "__main__":
    g = {'A': ['B', 'C'],
         'D': ['B'],
         'C': ['A'],
         'B': ['A', 'D']}

    gr = Graph(g)
    print(str(gr))
    gr.add_vertex('F')
    print(str(gr))
    gr.add_edge(('P', 'M'))
    print(str(gr))

    
        
        

