from graph import Graph
from collections import deque

def build_order(projects, dependencies):
    g = Graph()
    for proj in projects:
        g.add_node(proj, [proj, 0])
    for dep in dependencies:
        g.add_edge(dep[0], dep[1])
        g.nodes[dep[1]].data[1] += 1

    # get projects that have no dependencies (top projects)
    top = get_top_projects(g)

    order = []

    # get a build order for each top level project
    while top:
        proj = top.pop()
        if proj.data[0] not in visited:
            order.append(proj.data[0])
            visited.add(proj.data[0])
            edge_to_remove = []
            for dependent in proj.children:
                edge_to_remove.append((proj.key, dependent.key))
                dependent.data[1] -= 1
                if dependent.data[1] == 0:
                    top.append(dependent)
            for edge in edge_to_remove:
                g.rem_edge(*edge)


    return ', '.join(order)


def get_top_projects(g):
    top = []
    for proj in g.nodes.values():
        if not proj.data[1]:
            top.append(proj)
    return top

projects = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
dependencies = [('f', 'c'), ('f', 'b'), ('c', 'a'), ('b', 'a'), ('b', 'e'), ('a', 'e'), ('d', 'g')]
build_order(projects, dependencies)