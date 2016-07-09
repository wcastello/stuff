def B(k, n):
    return backtrack([], k, n, set())

def backtrack(s, k, n, seen):
    if (type(k) == int and len(s) == k**n) or (type(k) == str and len(s) == len(k)**n):
        if check_wrap(s, n, seen):
            return ''.join(map(str, s))
        return ''
    elif len(s) < n:
        try:
            candidates = list(range(k))
        except TypeError:
            candidates = list(k)

        for c in candidates:
            s.append(c)
            r =  backtrack(s, k, n, seen)
            if r:
                return r
            s.pop()
        return ''
    else:
        seen.add(''.join(map(str, s[-n:])))
        try:
            alphabet = list(range(k))
        except TypeError:
            alphabet = list(k)
        candidates = []
        for c in alphabet:
            if  ''.join(map(str, s[-(n-1):] + [c])) not in seen:
                candidates.append(c)
        for c in candidates:
            s.append(c)
            r = backtrack(s, k, n, seen)
            if r:
                return r
            s.pop()
        seen.remove(''.join(map(str, s[-n:])))
        return ''

def check_wrap(s, n, seen):
    for i in range(n-1):
        substr = ''.join(map(str, s[-(n-1)+i:] + s[0:i+1]))
        if substr in seen:
            return False
    return True
