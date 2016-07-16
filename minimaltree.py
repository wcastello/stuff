class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

class BTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insert_(self.root, data)

    def insert_(self, root, data):
        if not root:
            return Node(data)

        if data <= root.data:
            root.left = self.insert_(root.left, data)
        else:
            root.right = self.insert_(root.right, data)

        return root


def minimaltree(elems, tree):
    if not len(elems):
        return

    median_idx = (len(elems)-1)//2
    bottom = 0
    top = len(elems)

    tree.insert(elems[median_idx])
    minimaltree(elems[bottom:median_idx], tree)
    minimaltree(elems[median_idx+1:top], tree)


def minimaltree2(elems):
    if not len(elems):
        return BTree()

    median_idx = (len(elems)-1)//2
    bottom = 0
    top = len(elems)

    btree = BTree(Node(elems[median_idx]))
    btree.root.left = minimaltree2(elems[bottom:median_idx]).root
    btree.root.right = minimaltree2(elems[median_idx+1:top]).root

    return btree


def minimaltree3(elems):
    if not len(elems):
        return BTree()

    median_idx = (len(elems)-1)//2
    bottom = 0
    top = len(elems)

    btree = BTree()
    btree.insert(elems[median_idx])
    btree.root.left = minimaltree3(elems[bottom:median_idx]).root
    if btree.root.left:
        btree.root.left.parent = btree.root
    btree.root.right = minimaltree3(elems[median_idx+1:top]).root
    if btree.root.right:
        btree.root.right.parent = btree.root
    return btree


elems = list(range(1, 11))