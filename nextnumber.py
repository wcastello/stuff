def nextnumber(num):
    """ return a pair with the next smallest and next largest number with the
    same number of 1 bits as num
    """
    _ = num
    msbidx = 0
    while _ >> 1:
        _ >>= 1
        msbidx += 1 

    num_ones = 0
    for i in range(msbidx+1):
        curr = getbit(num, i)
        if curr:
            num_ones += 1
            if not getbit(num, i+1):
                smallest = setbit(num, i+1)
                print(smallest)
                # unset from bit i to 0
                smallest = unsetbitrange(smallest, i+1, 0)
                print(smallest)
                # set num_ones-1 bits on the left to 1
                smallest = setbitrange(smallest, num_ones-1, 0)
                print(smallest)
                break

    largest = 0
    for i in range(msbidx+1):
        if getbit(num, i):
            largest += 1 << msbidx+1
            msbidx -= 1

    return (smallest, largest)


def getbit(num, i):
    return num & (1 << i) != 0

def setbit(num, i):
    return num | (1 << i)

def unsetbit(num, i):
    return num & ~(1 << i)

def unsetbitrange(num, j, i):
    mask = (-1 << j) | ~(-1 << i)
    return num & mask

def setbitrange(num, j, i):
    mask = ~(-1 << j) & (-1 << i)
    return num | mask