from collections import deque

class Graph:
    def __init__(self, n):
        self.n = n
        self.vertices = n * [None]

    def add_edge(self, u, v, directed):
        if self.vertices[u]:
            self.vertices[u].append(v)
        else:
            self.vertices[u] = [v]
        if not directed:
            self.add_edge(v, u, directed=True)


def bicoloring(g):
    if g.n <= 0:
        return "N <= 0"

    visited = set()
    discovered = set()
    q = deque([0])
    color = {0: 'r'}
    while q:
        u = q.pop()
        discovered.add(u)
        for v in g.vertices[u]:
            if v not in discovered:
                color[v] = 'r' if color[u] == 'b' else 'b'
                discovered.add(v)
                q.appendleft(v)
            else:
                if v not in visited:
                    if color[v] == color[u]:
                        return "NOT BICOLORABLE."
        visited.add(u)
    return "BICOLORABLE."

def main():
    while True:
        n = int(input())
        if n == 0:
            return
        e = int(input())
        g = Graph(n)
        for j in range(e):
            u, v = map(int, input().split(' '))
            g.add_edge(u, v, directed=False)
        print(bicoloring(g))

if __name__ == '__main__':
    main()