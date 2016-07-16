def isrotation(a, b):
    """ Determine if string a b rotation of string a """
    if len(a) != len(b):
        return False

    for i in range(0, len(a)):
        x = a[:i]
        y = a[i:]
        print(x+y, y+x)
        if y + x == b:
            return True

    return False

# x + y is always a
# if b is a rotation of a, for some x and y, x + y = a and y + x = b
# y + x is a substring of x + y + x + y, that is, b is a substring of a + a
# it is enough to check then if b is a substring of a + a
def isrotation2(a, b):
    if (a+a).find(b) != -1:
        return True
    return False