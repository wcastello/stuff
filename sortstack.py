def sortstack(stack):
    if isEmpty(stack):
        return []
    sorteds = []
    top = pop(stack)
    if not isEmpty(stack):
        sorted_sub = sortstack(stack)
        if top > peek(sorted_sub):
            rev = reverse(sorted_sub)
            while not isEmpty(rev) and peek(rev) > top:
                push(sorteds, pop(rev))
            push(sorteds, top)
            while not isEmpty(rev):
                push(sorteds, pop(rev))
        else:
            sorteds = sorted_sub
            push(sorteds, top)
    else:
        push(sorteds, top)
    return sorteds

def sortstack2(stack):
    sortedstack = []
    while not isEmpty(stack):
        tmp = pop(stack)
        while not isEmpty(sortedstack) and tmp > peek(sortedstack):
            push(stack, pop(sortedstack))
        push(sortedstack, tmp)

    while not isEmpty(stack):
        push(sortedstack, pop(stack))

    return sortedstack


def sortstack3(stack):
    if len(stack) <= 1:
        return stack

    r = []
    mid = len(stack)//2
    leftstack = []
    rightstack = []
    for i in range(mid):
        push(leftstack, pop(stack))
    while not isEmpty(stack):
        push(rightstack, pop(stack))

    # each call to sortstack3() makes two more recursive calls with
    # half 
    leftsorted = sortstack3(leftstack)
    rightsorted = sortstack3(rightstack)
    print(leftsorted, rightsorted)

    # n
    while not isEmpty(leftsorted) and not isEmpty(rightsorted):
        if peek(leftsorted) <= peek(rightsorted): # n/2
            push(r, pop(leftsorted))
        else:
            push(r, pop(rightsorted))

    # n/2
    while not isEmpty(leftsorted): 
        push(r, pop(leftsorted))

    while not isEmpty(rightsorted):
        push(r, pop(rightsorted))

    print(r)
    r = reverse(r)
    print(r)
    return r

def mergesort(a):
    if len(a) == 1:
        return a

    left = mergesort(a[:len(a)//2])
    right = mergesort(a[len(a)//2:])

    r = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            r.append(left[i])
            i += 1
        else:
            r.append(right[j])
            j += 1

    r += left[i:]
    r += right[j:]

    return r

def sortedstack3(stack):
    pass

def isEmpty(stack):
    return len(stack) == 0

def push(stack, value):
    stack.append(value)

def pop(stack):
    return stack.pop()

def peek(stack):
    return stack[-1]

def reverse(stack):
    rev = []
    while not isEmpty(stack):
        push(rev, pop(stack))

    return rev

def permutations(seq):
    if len(seq) == 1 or not seq:
        return [seq]

    perms = []
    for e in seq:
        for perm in permutations([k for k in seq if k != e]):
            perms.append(perm + [e])

    return perms

# import random
# from time import time
# from math import inf
# import matplotlib.pyplot as plt

# def test(size):
#     best_t = inf
#     for perm in permutations(list(range(size))):
#         start_t = time()
#         sortstack(perm)
#         stop_t = time()
#         delta_t = stop_t - start_t
#         if delta_t < best_t:
#             best_t = delta_t
#     return best_t

# def test2(size):
#     start_t = time()
#     inp = list(range(size))
#     random.shuffle(inp)
#     sortstack(inp)
#     stop_t = time()
#     delta_t = stop_t - start_t
#     return delta_t

# def test3(size):
#     start_t = time()
#     inp = list(range(size))
#     random.shuffle(inp)
#     sortstack3(inp)
#     stop_t = time()
#     delta_t = stop_t - start_t
#     return delta_t

# def worst_times(maxsize):
#     worst_rtimes = []
#     for size in range(0, maxsize+1, 100):
#         worst_rtimes.append(round(test(size)*10000, 4))
#     return worst_rtimes

# def random_times(maxsize):
#     times = []
#     for size in range(maxsize+1):
#         times.append(round(test2(size), 4)*100)
#     return times

# def random_times2(maxsize):
#     times = []
#     for size in range(maxsize+1):
#         times.append(round(test3(size), 4)*100)
#     return times

# def plot(n):
#     for i in range(n):
#         plt.plot(worst_times(8))
#     plt.show()

# def plot2(n, maxsize):
#     for i in range(n):
#         plt.plot(random_times(maxsize))
#     plt.show()

# def plot3(n, maxsize):
#     for i in range(n):
#         plt.plot(random_times2(maxsize))
#     plt.show()
