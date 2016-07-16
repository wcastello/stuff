def strcompress(s):
    """ Compress the string s using the counts of repeated chars.
        Return a string where the repetitions of a char are substituted
        by the char followed by the number of repetitions.
        e.g strcompress(aaaccb) -> "a3c2b"
    """
    if not len(s):
        return ''

    sl = []
    last_char = s[0]
    count = 0
    for c in s:
        if c == last_char:
            count += 1
        else:
            sl.extend([last_char, str(count)])
            count = 1
        last_char = c
    sl.extend([last_char, str(count)])

    return ''.join(sl)