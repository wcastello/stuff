from collections import Counter

def unique(string):
    """ Determine if a string has all unique characters.
        Return True if it has, False otherwise.
    """
    for c in Counter(string).values():
        if c != 1:
            return False

    return True

def unique2(string):
    """ Determine if a string has all unique characters.
        Return True if it has, False otherwise.
    """
    chars = {}
    for c in string:
        if c in chars:
            return False
        chars[c] = True
    return True
