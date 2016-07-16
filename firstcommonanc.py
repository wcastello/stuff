from tree import BinaryTree

def first_common_anc(a, b):
    ancestors_a = set()
    ancestors_b = set()

    while a and b:
        if a.parent:
            ancestors_a.add(a.parent.data)
            print('adding ', a.parent.data)
            if a.parent.data in ancestors_b:
                return a.parent
        if b.parent:
            ancestors_b.add(b.parent.data)
            print('adding ', b.parent.data)
            if b.parent.data in ancestors_a:
                return b.parent
        a = a.parent
        b = b.parent

    while a:
        print('checking ', a.parent.data)
        if a.parent.data in ancestors_b:
            return a.parent
        a = a.parent
    while b:
        print('checking ', b.parent.data)
        if b.parent.data in ancestors_a:
            return b.parent
        b = b.parent

    return None # different trees or one of the nodes is the top node

def depth(node):
    if not node:
        return -1
    return depth(node.parent) + 1

def first_common_anc2(a, b):
    d = depth(a) - depth(b)
    if d <= 0: a, b = b, a  # a is the the deeper node

    for i in range(abs(d)):
        print(a.data)
        a = a.parent

    while a and b and a != b:
        a = a.parent
        b = b.parent

    return a if a and b else None


def first_common_anc3(a, b):
    if covers(a, b):
        return a
    elif covers(b, a):
        return b

    curr = a.parent
    past = a

    while curr:
        if curr.left != past:
            if covers(curr.left, b):
                return curr
        else:
            if covers(curr.right, b):
                return curr
        past = curr
        curr = curr.parent

    return None


def covers(root, node):
    """ Check if node is covered by the tree rooted at root """
    if not root:
        return False
    if root == node:
        return True
    return covers(root.left, node) or covers(root.right, node)
