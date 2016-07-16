class Node:
    def __init__(self, data=None, root=None):
        self.data = data
        self.parent = root
        self.left = None
        self.right = None

class BTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.root = self.insert_(data, self.root)

    def insert_(self, data, root=None):
        if not root:
            return Node(data)

        if data <= root.data:
            root.left = self.insert_(data, root.left)
        else:
            root.right = self.insert_(data, root.right)

from collections import deque
def listOfDepths(bt):
    q = deque([(bt.root, 0)])
    visited = set()
    nodes_depth = []

    while q:
        node, depth = q.pop()
        if node.data not in visited:
            visited.add(node.data)
            if len(nodes_depth) <= depth:
                nodes_depth.append([])
            nodes_depth[depth].append(node.data)
            if node.left and node.left.data not in visited:
                q.appendleft((node.left, depth+1))
            if node.right and node.right.data not in visited:
                q.appendleft((node.right, depth+1))

    return nodes_depth

# instead of keeping track of the depths just move one at a time
def listOfDepths2(bt):
    data_depth = []
    level = 0
    next_children = [bt.root]
    while next_children:
        data_depth.append([])
        children = next_children
        next_children = []
        for child in children:
            if child: 
                data_depth[level].append(child.data)
                if child.left: next_children.append(child.left)
                if child.right: next_children.append(child.right)
        level += 1
    return data_depth