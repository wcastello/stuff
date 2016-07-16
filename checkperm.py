def checkperm(a, b):
    """ Check if string a is a permutation of string b
        Return True if so, otherwise return False """
    if len(a) != len(b):
        return False

    t_a, t_b = {}, {}

    for c, k in zip(a, b):
        t_a[c] = t_a.get(c, 0) + 1
        t_b[k] = t_b.get(k, 0) + 1

    return t_a == t_b

def checkperm2(a, b):
    return sorted(a) == sorted(b)