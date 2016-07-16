from collections import deque

def check_subtree(t1, t2):
    # traverse t1 breadth-first looking for the root of t2
    if not t1.root:
        return False
    elif not t2.root:
        return True

    q = deque([t1.root])
    visited = set()
    # worst case we examine all the nodes on t1 looking for t2.root
    # this runs in O(n), so the whole algorithm run time is O(n + km) and takes O(n + log(m)) ~ O(n) space
    while q:
        n = q.pop()
        if n and n.data == t2.root.data:
            # match is called k times, k being the number of times 
            # t2.root appears on t1
            # each match() checks all the nodes on t2 if the two trees 
            # are equivalent
            if match(n, t2.root):
                return True
        if n not in visited:
            visited.add(n)
            if n.left: q.appendleft(n.left)
            if n.right: q.appendleft(n.right)

    return False

# improved space complexity O(log(n) + log(m))
def check_subtree2(t1, t2):
    if not t1.root:
        return False
    elif not t2.root:
        return True

    # t2 can be a subtree of t1.left, t2.right, the t1 tree itself or none
    if (t1.root.data == t2.root.data) and match(t1.root, t2.root):
        return True

    return check_subtree(BTree(t1.root.left), t2) or check_subtree(BTree(t1.root.right), t2)

# O(m) time, O(log(m)) space 
def match(n, m):
    if not n and not m:
        return True
    if not n or not m:
        return False

    # if n.data != m.data it won't recur, it they're equal but the first match is false 
    # the second call won't happen either
    return n.data == m.data and match(n.left, m.left) and match(n.right, m.right)