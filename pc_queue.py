def main():
    memo = {}
    t = int(input())
    for i in range(t):
        n, p, q = map(int, input().split())
        print(queue_perms(n, p, q, memo))

def queue(n, p, r):
    nsols = {}
    nsols[(n, p, r)] = 0
    backtrack(n*[-1], n, 0, p, r, 0, -1, nsols)
    return nsols[(n, p, r)]

def backtrack(a, n, k, p, r, p_, tallest, nsols):
    if p_ > p or n - k < p - p_:
        return
    elif n == k and p_ == p:
        if count_r(a) == r:
            nsols[(n, p, r)] += 1
    else:
        candidates = set(range(n)) - set(a[:k])
        k += 1
        for c in candidates:
            p__ = p_
            tallest_ = tallest
            if c > tallest:
                p__ = p_ + 1
                tallest_ = c
            a[k-1] = c
            backtrack(a, n, k, p, r, p__, tallest_, nsols)

def queue_perms(n, p, r, memo):
    if (n, p, r) in memo:
        return memo[(n, p, r)]
    elif n == p == r == 1 or n == p == r == 0:
        perms = 1
    elif p + r > n + 1 or p + r < 2:
        perms = 0
    else:
        perms = 0
        for i in range(p, n-r+2):
            left_perms = binomial(n-1, i-1, memo) * sum([queue_perms(i-1, p-1, j, memo) for j in range(0, i)])
            right_perms = sum([queue_perms(n-i, j, r-1, memo) for j in range(0, n-i+1)])
            perms += left_perms * right_perms

    memo[(n, p, r)] = perms
    return perms

def binomial(n, k, memo):
    if k == 0 or k == n:
        return 1
    elif n < k or n < 0 or k < 0:
        return 0
    else:
        return memo.setdefault((n-1, k-1), binomial(n-1, k-1, memo)) + \
                memo.setdefault((n-1, k), binomial(n-1, k, memo))

def count_r(a):
    r = 0
    tallest = -1
    for x in reversed(a):
        if x > tallest:
            tallest = x
            r += 1
    return r

if __name__ == '__main__':
    main()
