# O(n) time, O(n) space, will preserve order
def removedups(li):
    """ Remove duplicates from a list.
        Return new list without duplicates.
    """
    seen = set()
    return [(lambda x: seen.add(x) or x)(x) for x in li if x not in seen]


# O(n), but faster, won't preserve order
def removedups2(li):
    s = set()
    for x in li:
        s.add(x)
    return list(s)


# O(n), but much faster, won't preserve order
def removedups3(li):
    return list(set(li))


# without additional space
def removedups4(li):
    i = 0
    k = len(li)
    while i < k:
        j = i + 1
        while j < k: # j index runner
            if li[j] == li[i]:
                li.pop(j) # no duplicates, no pops, for each duplicate one pop -> O(n)
                j -= 1    # at most n-1 duplicates -> n-1 pops, O(n^2)
                k -= 1
            j += 1
        i += 1

# for d duplicates, the outer while runs n - d times
# for a maximum of n - 1 duplicates the outer while runs 1 time
# and the inner while n - 1 times and performs n - 1 pops which are O(n), so O(n^2)

