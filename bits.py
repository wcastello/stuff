def getbit(n, i):
    return n & (1 << i) != 0 # could be without the != 0 to get the whole number

def setbit(n, i):
    return n | (1 << i)

def clearbit(n, i):
    mask = ~(1 << i)
    return n & mask

def clearbitsMSBthroughI(n, i):
    mask = (1 << i) - 1
    return n & mask

def clearbitsMSBthroughI2(n, i):
    mask = ~(-1 << i)
    return n & mask

def updatebit(n, i, bit_is_one):
    if bit_is_one:
        clearbit(n, i)
    else:
        setbit(n, i)