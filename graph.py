class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.children = []

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, key, data):
        self.nodes[key] = Node(key, data)

    def add_uedge(self, key_a, key_b):
        self.nodes[key_a].children.append(self.nodes[key_b])
        self.nodes[key_b].children.append(self.nodes[key_a])

    def add_edge(self, key_a, key_b):
        self.nodes[key_a].children.append(self.nodes[key_b])

    def rem_edge(self, key_a, key_b):
        self.nodes[key_a].children.remove(self.nodes[key_b])