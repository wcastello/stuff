from collections import Counter

def is_permut_palin(string):
    c = Counter(string.lower())
    len_ = len(string)

    rem_one = 0
    for k in c.values():
        if k % 2 != 0 > 1:
            return False
        elif k % 2 == 1:
            rem_one += 1
            if rem_one != 1:
                return False

    return True