# A queue with two stacks
class MyQueue:
    def __init__(self):
        self.stackA = []
        self.stackB = []

    def enqueue(self, data):
        self.stackA.append(data)

    def dequeue(self):
        if len(self.stackB) == 0:
            if len(self.stackA):
                self.reverse_stacks_()
            else:
                raise IndexError('dequeue from empty queue')

        return self.stackB.pop()

    def reverse_stacks_(self):
        while len(self.stackA) > 0:
            self.stackB.append(self.stackA.pop())