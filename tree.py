import random

class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.size = 1
        self.parent = parent
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.root = self.insert_(data, self.root, self.root)

    def insert_(self, data, parent, root):
        if not root:
            return Node(data, parent)

        if random.randint(0, 1):
            root.left = self.insert_(data, root, root.left)
        else:
            root.right = self.insert_(data, root, root.right)

        return root

class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.root = self.insert_(data, self.root, self.root)

    def insert_(self, data, parent, root):
        if not root:
            return Node(data, parent)

        if data <= root.data:
            root.left = self.insert_(data, root, root.left)
        else:
            root.right = self.insert_(data, root, root.right)

        return root

class RandBinaryTree:
    def __init__(self, root=None):
        self.root = root
        self.length = 0

    def insert(self, data):
        self.length += 1
        if not self.root:
            self.root = Node(data)
        else:
            self.root = self.insert_(data, self.root, self.root)

    def insert_(self, data, parent, root):
        if not root:
            return Node(data, parent)

        if not root.left:
            root.left = self.insert_(data, root, root.left)
        elif not root.right:
            root.right = self.insert_(data, root, root.right)
        else:
            if root.left.size <= root.right.size:
                root.left = self.insert_(data, root, root.left)
            else:
                root.right = self.insert_(data, root, root.right)

        root.size += 1
        return root

    def delete(self, data):
        pass

    # O(n) in time, O(log(n)) space
    def get_random_node(self):
        """ randomly select a number x between 0 and n-1, with n being the number of
            nodes in the tree and then use get_node(x) to return this node """

        x = random.randint(0, self.length-1)
        return self.get_node(x)

    def get_node(self, n):
        def get_node_helper(root, n, i, c):
            if root:
                print('\t'*c + '*')
                if i == n:
                    return root, i
                if root.left:
                    found, i = get_node_helper(root.left, n, i+1, c+1)
                    if found:
                        return found, i
                if root.right:
                    found, i = get_node_helper(root.right, n, i+1, c+1)
                    if found:
                        return found, i
            return None, i
        return get_node_helper(self.root, n, 0)[0]

    # each node holds the size of its own subtree
    # O(log(n)) in time in a balanced tree, O(1) in space.
    # For sufficient big n RandBinaryTree is balanced since the insertions go to a randomly
    # side on each step of insert_()
    def get_random_node2(self):
        root = self.root
        while root:
            r = random.random()
            if 0 <= r < 1/root.size:
                return root
            elif root.left and 1/root.size <= r < 1/root.size + root.left.size/root.size:
                root = root.left
            elif root.right:
                root = root.right



def count_paths_with_sum(root, s):
    if not root:
        return 0


    paths_here = count_paths(root, s, 0)
    paths_left = count_paths_with_sum(root.left, s)
    paths_right = count_paths_with_sum(root.right, s)

    return paths_here + paths_left + paths_right

def count_paths(node, s, total):
    if not node:
        return 0

    paths = 0
    total += node.data
    if total == s:
        paths += 1

    paths += count_paths(node.left, s, total)
    paths += count_paths(node.right, s, total)

    return paths


def subarray_with_sum(arr, target):
    sums_count = {0:1}
    total = 0
    target_count = 0
    for x in arr:
        total += x
        if total-target in sums_count:
            target_count += sums_count[total-target]
        sums_count[total] = sums_count.get(total, 0) + 1

    return target_count


def count_paths_with_sum2(root, s):
    if not root:
        return 0
    return count_paths2(root, s, 0, {})

def count_paths2(node, s, total, memo):
    if not node:
        return 0

    paths = 0

    total += node.data
    if total == s:
        paths += 1

    if total-s in memo:
        paths += memo[total-s]

    memo[total] = memo.get(total, 0) + 1

    paths += count_paths2(node.left, s, total, memo)
    paths += count_paths2(node.right, s, total, memo)

    memo[total] -= 1

    return paths