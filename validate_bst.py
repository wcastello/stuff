from math import nan

# leverage the fact that a binary tree when traversed in-order dfs is ordered
def validateBST(root):
    """ Check if a binary tree is a binary search tree """
    if not root:
        return True

    s = [root]
    n = root
    visited = set()
    last = nan
    # iterative in-order dfs
    while s:
        if n.left and n.left not in visited:
            s.append(n.left)
            n = n.left
            continue
        n = s.pop()
        if n.data <= last:
            print(n.data, last)
            return False
        last = n.data
        visited.add(n)
        if n.right and n.right not in visited:
            s.append(n.right)
            n = n.right
            continue
    
    return True

def inorder_traversal_iter(root):
    if not root:
        return

    s = [root]
    n = root

    while s:
        while n.left:
            s.append(n.left)
            n = n.left
        n = s.pop()
        print(n.data)
        if n.right:
            s.append(n.right)
            n = n.right

def inorder_traversal_iter2(node):
    s = []

    while s or node:
        if node:
            s.append(node)
            node = node.left
        else:
            node = s.pop()
            print(node.data)
            node = node.right

def preorder_traversal_iter2(node):
    if not node:
        return
        
    s = [node]

    while s:
        node = s.pop()
        print(node.data)
        if node.right:
            s.append(node.right)
        if node.left:
            s.append(node.left)