def urlify(string):
    """ Replace all whitespaces with %20 and return the new string """
    return string.replace(' ', '%20')

def urlify2(string):
    return ''.join(['%20' if c == ' ' else c for c in string])

def urlify3(string):
    strlist = list(string)
    ws = 0
    for c in string:
        if c == ' ':
            ws += 1
    len_ = len(string)
    j = len_ + 2 * ws
    strlist += 2 * ws * ['']

    for i in range(len_):
        if strlist[len_ - i] == ' ':
            strlist[j-1] = '0'
            strlist[j-2] = '2'
            strlist[j-3] = '%'
            j -= 3
        else:
            strlist[j-1] = strlist[len_ - i]
            j -= 1

    return ''.join(strlist)