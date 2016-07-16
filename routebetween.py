class Node:
    def __init__(self, data=None):
        self.data = data
        self.children = []

class Graph:
    def __init__(self, nodes=[]):
        self.nodes = nodes

    def add_node(self, node):
        self.node.append(node)

    def add_uedge(self, a, b):
        a.children.append(b)
        b.children.append(a)

    def add_edge(self, a, b):
        a.children.append(b)

def dfs(vertex):
    s = [vertex]
    seen = set()
    while s:
        node = s.pop()
        if node.data not in seen:
            seen.add(node.data)
            print('{} '.format(node.data), end='')
            for c in node.children:
                if c not in seen:
                    s.append(c)

def dfs_r(vertex, seen):
    if vertex.data in seen:
        return
    print(vertex.data)
    seen.add(vertex.data)
    for c in vertex.children:
        dfs_r(c, seen)

from collections import deque
def bfs(vertex):
    q = deque([vertex])
    seen = set()
    while q:
        node = q.pop()
        if node.data not in seen:
            seen.add(node.data)
            print('{} '.format(node.data), end='')
            for c in node.children:
                if c.data not in seen:
                    q.appendleft(c)


def routebetween(g, v1, v2):
    s = v1.children
    seen = set()
    while s:
        node = s.pop()
        if node.data not in seen:
            seen.add(node.data)
            if node.data == v2.data:
                return True
            for c in node.children:
                s.append(c)
    return False

n = 5
nodes = [Node(i) for i in range(n)]
g = Graph(nodes)
for i in range(n):
    for j in range(i+1, n):
        g.add_uedge(g.nodes[i], g.nodes[j])

# tree graph
n2 = 8
nodes2 = [Node(i) for i in range(n2)]
g2 = Graph(nodes2)
g2.add_uedge(g2.nodes[0], g2.nodes[1])
g2.add_uedge(g2.nodes[1], g2.nodes[2])
g2.add_uedge(g2.nodes[1], g2.nodes[3])
g2.add_uedge(g2.nodes[2], g2.nodes[4])
g2.add_uedge(g2.nodes[2], g2.nodes[5])
g2.add_uedge(g2.nodes[4], g2.nodes[6])
g2.add_uedge(g2.nodes[5], g2.nodes[7])

# directed graph:
n3 = 5
nodes3 = [Node(i) for i in range(n3)]
g3 = Graph(nodes3)
g3.add_edge(nodes3[0], nodes3[1])
g3.add_edge(nodes3[1], nodes3[3])
g3.add_edge(nodes3[3], nodes3[2])
g3.add_edge(nodes3[2], nodes3[4])
g3.add_edge(nodes3[2], nodes3[3])
g3.add_edge(nodes3[4], nodes3[2])
