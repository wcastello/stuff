class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, node):
        if not self.head:
            self.head = node
        else:
            tmp = self.head
            self.head = node
            node.next = tmp

    def find(self, data):
        curr = self.head
        while curr:
            if curr.data == data:
                return True
            curr = curr.next
        return False

    def __iter__(self):
        self.e = self.head
        return self

    def __next__(self):
        if not self.e:
            raise StopIteration
        data = self.e.data
        self.e = self.e.next
        return data

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

class Array:
    def __init__(self, size=0):
        self.size = size
        self.data = size * [None]

    def __getitem__(self, idx):
        return self.data[idx]

    def __setitem__(self, idx, value):
        self.data[idx] = value

class HashTable:
    def __init__(self, hashfn, numBuckets=1000):
        self.hashfn = hashfn
        self.numBuckets = numBuckets
        self.bucket = Array(numBuckets)
        self._keys = LinkedList()


    def insert(self, value):
        key = self.hashfn(value) % self.numBuckets
        if self.bucket[key]:
            if self.bucket[key].find(value):
                raise ValueError('Trying to insert duplicated value.')
            self.bucket[key].append(Node(value))
        else:
            self.bucket[key] = LinkedList(Node(value))
            self._keys.append(Node(key))

    def find(self, value):
        key = self.hashfn(value) % self.numBuckets
        if self.bucket[key]:
            return self.bucket[key].find(value)
        return False

    @property
    def keys(self):
        return str(self._keys)

    def values(self):
        allvalues = LinkedList()
        for key in self._keys:
            for data in self.bucket[key]:
                allvalues.append(Node(data))

        return str(allvalues)

def processSearch(query):
    result, lastUpdate = getFroCache(query)
    if result and timeDelta(lastUpdate) > 60:
        result = getResult(query)
        updateCache(query, result)

    return result


def getFromCache(query):
    pass


def updateCache(query, result):
    pass