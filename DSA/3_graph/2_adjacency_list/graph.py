class Graph:

    def __init__(self, num_of_nodes, directed=True):
        self.num_of_nodes = num_of_nodes
        self.nodes = range(self.num_of_nodes)
        self.directed = directed
        self.adj_list = {node: set() for node in self.nodes}

    def add_edge(self, node1, node2, weight=1):
        self.adj_list[node1].add((node2, weight))
        if not self.directed:
            self.adj_list[node1].add((node2, weight))

    def print_adj_list(self):
        for key in self.adj_list.keys():
            print("node", key, ": ", self.adj_list[key])