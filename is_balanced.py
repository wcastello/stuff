from btree import BTree

def is_balanced(root):
    """ Check if a Binary tree is balanced (heights of subtrees of any node do not 
        differ by more than one).
        Return True if it is, False otherwise.
    """
    if not root:
        return True

    if (root.left and not root.right) or \
        (not root.left and root.right):
        return abs(depth(root.left) - depth(root.right)) <= 1

    return is_balanced(root.left) and is_balanced(root.right)

def depth(root):
    if not root:
        return 0
    return max(depth(root.left), depth(root.right)) + 1


# The following are from "Cracking the code interview"
# I'd say mine is clearer
def checkHeight(root):
    if not root:
        return -1

    print(root.data)
    lheight = checkHeight(root.left)
    if lheight == -2: return -2

    rheight = checkHeight(root.right)
    if rheight == -2: return -2

    if abs(lheight - rheight) > 1:
        return -2
    return max(lheight, rheight) + 1

def is_balanced2(root):
    return checkHeight(root) != -2