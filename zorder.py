# this is ridiculous.

def zorder(x, y, size):
    # make sure we're not out of bounds and using a power of 2 size
    # could've used the bitcount() from problem 1 to assert for the power of 2.
    assert size > 0 and bin(size).count('1') == 1, 'size >= 0 should be a power of 2'
    assert 0 <= x < size and 0 <= y < size, 'x and y should be in [0, size)'

    # base case
    if size == 1:
        return 0

    # get quadrant of (x, y)
    offset = { (0, 0): 0, (1, 0): (size//2)**2, (0, 1): 2*(size//2)**2, (1, 1): 3*(size//2)**2 }
    q_x = x//(size//2)
    q_y = y//(size//2)

    # takes size from 2^n -> 2^(n-1), O(log_2(n)) time.
    return offset[(q_x, q_y)] + zorder(x%(size//2), y%(size//2), size//2)


def print_grid(size):
    for i in range(size):
        row = []
        for j in range(size):
            row.append(str(zorder(j, i, size)))
        print(' '.join(row))

# zorder(4, 3, 8)
# 37

# zorder(0, 0, 2)
# 0

# print_grid(4)
# 0 1 4 5
# 2 3 6 7
# 8 9 12 13
# 10 11 14 15

# print_grid(8)
# 0 1 4 5 16 17 20 21
# 2 3 6 7 18 19 22 23
# 8 9 12 13 24 25 28 29
# 10 11 14 15 26 27 30 31
# 32 33 36 37 48 49 52 53
# 34 35 38 39 50 51 54 55
# 40 41 44 45 56 57 60 61
# 42 43 46 47 58 59 62 63