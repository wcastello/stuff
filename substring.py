def substr(string, substring):
    for i in range(len(string)-len(substring)):
        for j in range(len(substring)):
            if substring[j] != string[i+j]:
                break
        else:
            return i
    return -1

def substr2(string, substring):
    for i in range(len(string)-len(substring)+1):
        diff = False
        for j in range(len(substring)):
            if substring[j] != string[i+j]:
                diff = True
                break
        if diff:
            continue
        return i
    return -1

def rolling_hash(string, substr_size):
    bhs = ord(string[0])
    hs = sum([ord(string[i]) for i in range(substr_size)]) # O(m), only once
    yield hs
    for i in range(1, len(string)-substr_size+1): # O(n)
        bhs = ord(string[i-1]) # O(1)
        hs = hs - bhs + ord(string[substr_size+i-1]) # O(1)
        yield hs

# Average and best-case running time O(m+n) in space O(1)
# Worst-case running time O(n*m), in case we compare the hash function is really bad and
# we have to compare it n times, thus comparing the strings (which is O(m)) n times.
def rabin_karp(string, substring):
    hsub = sum([ord(c) for c in substring]) # O(m), only once
    for i, hs in enumerate(rolling_hash(string, len(substring))): # O(n)
        if hsub == hs: # Expected to run only once if hash is good enough
            # print('compared hash!')
            if string[i:i+len(substring)] == substring: # O(m)
                return i
    return -1