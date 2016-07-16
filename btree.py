from linkedlist import Node, LinkedList

class Node:
    def __init__(self, data=None, parent=None):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None

class BTree:
    def __init__(self, root=None):
        self.root = root

    def insert_iter(self, node):
        if not self.root:
            self.root = node
            return 

        curr = self.root
        while curr:
            if node.value <= curr.value:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = node
                    break
            else:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = node
                    break

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

    def inOrder_(self, root):
        if root is not None:
            self.inOrder_(root.left)
            print(root.data, end='')
            self.inOrder_(root.right)

    def preOrder_(self, root):
        if root is not None:
            print(root.data, end='')
            self.preOrder_(root.left)
            self.preOrder_(root.right)        

    def postOrder_(self, root):
        if root is not None:
            self.postOrder_(root.left)
            self.postOrder_(root.right)
            print(root.data, end='')

    def traverse(self, order='inOrder', root=None):
        orderfn = {
            'inOrder': self.inOrder_,
            'preOrder': self.preOrder_,
            'postOrder': self.postOrder_,
        }

        if root is None:
            orderfn[order](self.root)
        else:
            orderfn[order](root)  

def listOfDepth(root, depth):
    if depth == 0:
        if root:
            return LinkedList(Node(root.data))
        else:
            return LinkedList()

    leftList = LinkedList()
    rightList = LinkedList()

    if root.left:
        leftList = listOfDepth(root.left, depth-1)
    if root.right:
        rightList = listOfDepth(root.right, depth-1)


    # LinkedList without a tail:
    curr = leftList.head
    tail = curr
    while curr:
        tail = curr
        curr = curr.next
    
    if tail:
        tail.next = rightList.head
    else:
        leftList = rightList

    return leftList


def listOfDepth2(root, depth):
    if depth == 0:
        if root:
            return LinkedList(Node(root.data))
        else:
            return LinkedList()

    leftList = LinkedList()
    rightList = LinkedList()

    if root.left:
        leftList = listOfDepth(root.left, depth-1)
    if root.right:
        rightList = listOfDepth(root.right, depth-1)

    if leftList.tail:
        leftList.tail.next = rightList.head
        leftList.tail = rightList.tail
    else:
        leftList = rightList

    return leftList