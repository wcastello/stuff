from btree import BTree, Node

def successor(node):
    # get root of tree:
    curr = node
    while curr.parent:
        curr = curr.parent

    # traverse in order until we find node and then get the next on stack
    s = []
    successor = None
    found = False
    while s or curr:
        if curr:
            s.append(curr)
            curr = curr.left
        else:
            curr = s.pop()
            if found:
                successor = curr
                break
            if curr.data == node.data:
                found = True
            curr = curr.right

    return successor

def successor2(node):
    # if there is a left subtree then it's the first visited in-order
    if node.right:
        curr = node.right
        while curr.left:
            curr = curr.left
        return curr
    # otherwise it's the first parent which can be arrived from the left
    else:
        curr = node.parent
        while curr: # this could be "and (curr.left and curr.left.data != ...)" then we would leave when ==
            if curr.left and curr.left.data == node.data:
                break
            node = curr
            curr = curr.parent
        return curr


t = BTree()
t.insert(5)
t.insert(3)
t.insert(7)
t.insert(-1)
t.insert(4)
t.insert(6)
t.insert(8)
t.insert(-2)
t.insert(2)
t.insert(0)
t.insert(1)

node = t.root.left.left.right.left # 0, successor is 1

successor(node)