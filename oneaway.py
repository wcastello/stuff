def oneaway(sa, sb):
    """ Given two strings sa and sb check if they're 
        one insert, replace or remove away from each other.
        Return True if they are, otherwise return False.
    """
    if abs(len(sa) - len(sb)) > 1:
        return False

    if sa == sb:
        return True 

    if len(sa) < len(sb):
        sa, sb = sb, sa

    for i in range(len(sb)):
        if sa[i] != sb[i]:
            if len(sa) == len(sb):
                return sa[i:] == sa[i] + sb[i+1:]
            else:
                return sa[i+1:] == sb[i:]

    return True;