class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.tail = head
        self.length = 1 if head else 0

    def append(self, node):
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1

    # def append_end(self, node):
    #     if self.length == 0:
    #         self.head = node
    #     else:
    #         curr = self.head
    #         while curr:
    #             past = curr
    #             curr = curr.next
    #         past.next = node
    #     self.length += 1

    def append_end(self, node):
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next

    def find(self, data):
        curr = self.head
        while curr:
            if curr.data == data:
                return True
            curr = curr.next
        return False


    def merge(self, b):
        self.tail.next = b.head
        self.tail = b.tail

    # O(n)
    def remove_dups(self):
        curr = self.head
        counter = {}

        while curr: # O(n)
            counter[curr.data] = counter.get(curr.data, 0) + 1
            curr = curr.next

        curr = self.head
        prev = None
        while curr: # O(n)
            if counter[curr.data] > 1: # O(1)
                if prev:
                    counter[curr.data] -= 1 # O(1)
                    del prev.next
                    self.length -= 1
                    prev.next = curr.next
                    curr = prev.next
            prev = curr
            curr = curr.next


    # Running time O(n) in one pass with O(n) space
    def remove_dups2(self):
        seen = set()
        curr = self.head
        prev = None
        while curr: # O(n)
            if curr.data in seen:  # O(1)
                del prev.next
                prev.next = curr.next
                curr = prev.next
            seen.add(curr.data)  # O(1)
            prev = curr
            curr = curr.next


    # faster, just one pass
    def kth_to_last(self, k):
        p = self.head
        q = self.head
        for i in range(k+1):
            if not p:
                return None
            p = p.next

        while p:
            p = p.next
            q = q.next
        return q


    def remove_middle(self, node):
        if not node or not node.next:
            return False
        node.next = node.next.next
        self.length -= 1
        # there is not reference to the old node.next anymore, so Python will collect the garbage
        return True


    def partition(self, data):
        left = LinkedList()
        left_tail = None
        right = LinkedList()
        curr = self.head

        while curr:
            node = Node(curr.data)
            if curr.data < data:
                if not left.head:
                    left_tail = node
                left.append(node)
            else:
                right.append(node)
            curr = curr.next

        if left_tail:
            left_tail.next = right.head
        else:
            left = right

        return left

    def copy(self):
        cpy = LinkedList()
        curr = self.head
        while curr:
            cpy.append_end(Node(curr.data))
            curr = curr.next

        return cpy

    # digits in backward order, head has smallest value
    def sum_list(self, listb=None):
        if not listb:
            return self

        result = LinkedList()
        a = self.head
        b = listb.head


        def sumloop(nodes, result, carry):
            n = len(nodes)
            while all(nodes):
                sumdig = sum([nodes[i].data for i in range(n)])
                if carry:
                    sumdig += 1
                if sumdig//10:
                    carry = True
                else:
                    carry = False
                dig = sumdig % 10
                result.append(Node(dig))
                for i in range(n):
                    nodes[i] = nodes[i].next
            return (*nodes), carry

        a, b, carry = sumloop([a, b], result, False)

        a = a or b
        if not a and carry:
            result.append(Node(1))
        else:
            sumloop([a, ], result, carry)

        reverse = LinkedList()
        curr = result.head
        while curr:
            reverse.append(Node(curr.data))
            curr = curr.next

        return reverse


    # digits in forward order, head has the greatest value
    def sum_list2(self, listb=None):
        if not listb:
            return self


    def __str__(self):
        s = '['
        curr = self.head
        while curr:
            s += repr(curr.data)
            if curr.next:
                s += ', '
            curr = curr.next
        s += ']'
        return s


    def __repr__(self):
        return 'LinkedList({})'.format(str(self))


def pyListToLList(pyList):
    l = LinkedList()
    for e in pyList:
        l.append(Node(e))
    return l

def sumList(a, b):
    if not a.length or not b.length:
        return a if a.length else b

    def sumListHelper(node_a, node_b, carry):
        result = None
        if not node_a and not node_b:
            if carry:
                result = Node(carry)
            return result
        if not node_a:
            dig_a = 0
            next_a = None
        else:
            dig_a = node_a.data
            next_a = node_a.next
        if not node_b:
            dig_b = 0
            next_b = None
        else:
            dig_b = node_b.data
            next_b = node_b.next
        sumdig = dig_a + dig_b + carry
        dig = sumdig % 10
        carry = sumdig // 10

        result = Node(dig)
        result.next = sumListHelper(next_a, next_b, carry)
        return result

    return LinkedList(sumListHelper(a.head, b.head, 0))

def sumList2(a, b):
    if not a.length or not b.length:
        return a if a.length else b

    if a.length < b.length:
        a, b = b, a
    else:
        lendiff = a.length - b.length
        b = b.copy()
        curr = b.head
        while lendiff:
            b.append(Node(0))
            curr = curr.next
            lendiff -= 1

    def sumListHelper(node_a, node_b):
        result = None
        if not node_a and not node_b:
            return result, 0

        tmp, carry = sumListHelper(node_a.next, node_b.next)
        sumdig = node_a.data + node_b.data + carry
        dig = sumdig % 10
        carry = sumdig // 10
        result = Node(dig)
        result.next = tmp 

        return result, carry

    result, carry = sumListHelper(a.head, b.head)
    if carry:
        result.append(Node(carry))

    return LinkedList(result)

def is_palin(li):
    curr = li.head
    fast = li.head
    reverse = LinkedList() # use reverse as a stack with appends
    while fast:
        reverse.append(Node(curr.data))
        if fast.next:
            fast = fast.next.next
        else:
            break
        curr = curr.next

    fast = li.head
    curr_rev = reverse.head
    while fast:
        if curr.data != curr_rev.data:
            return False
        curr = curr.next
        if fast.next:
            fast = fast.next.next
        else:
            fast = fast.next
        curr_rev = curr_rev.next # we're basically pop()ing here

    return True

def list_len(li):
    length = 0
    curr = li.head
    while curr:
        length += 1
        curr = curr.next
    return length

def is_palin_R(li):
    length = list_len(li)

    def recur(node, length):
        if length == 1:
            return (node.next, True)
        elif length == 0:
            return (node, True)

        retnode, _ = recur(node.next, length-2)

        if retnode and node.data == retnode.data:
                return (retnode.next, True)

        return (None, False)

    return recur(li.head, length)[1]


def intersects(a, b):
    d = a.length - b.length
    if d > 0: a, b = b, a  # let a be the smallest list
    print(d)
    # advance the different on the biggest list b
    curr_b = b.head
    for i in range(abs(d)):
        curr_b = curr_b.next

    curr_a = a.head
    # check if any of the nodes intersect
    while curr_a and curr_b:
        if curr_a == curr_b:
            return curr_a
        curr_a = curr_a.next
        curr_b = curr_b.next

    # reached end of the lists, no intersection
    return None

def find_loop(li):
    seen = set()
    curr = li.head
    while curr:
        if id(curr) in seen:
            return curr
        seen.add(id(curr))
        curr = curr.next
    return None

l = LinkedList()
l.append(Node(6))
l.append(Node(1))
l.append(Node(7))

l2 = LinkedList()
l2.append(Node(2))
l2.append(Node(9))
l.sum_list(l2)