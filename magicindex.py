# naive solution
def magicindex(li):
    for i in range(len(li)):
        if i == li[i]:
            return i

    return -1

# binary search
def magicindex(li):
    maxidx = len(li)-1
    minidx = 0
    idx = maxidx

    while maxidx - minidx >= 0:
        if idx == li[idx]:
            return idx
        elif idx > li[idx]:
            minidx = idx+1
        else:
            maxidx = idx-1
        idx = (maxidx + minidx)//2

    return -1

def binsearch(li, e):
    l = 0
    r = len(li)-1
    while r - l >= 0:
        m = (l + r)//2
        if li[m] == e:
            return True
        elif li[m] > e:
            r = m-1
        else:
            l = m+1
        print(m, l, r)

def binsearchr(li, e, l, r):
    print(e, l, r)
    if r - l < 0:
        return False

    m = (l + r)//2
    if li[m] == e:
        return True
    elif li[m] > e:
        return binsearchr(li, e, l, m-1)
    else:
        return binsearchr(li, e, m+1, r)