parent = 6*[None]
parent[5] = 3
parent[3] = 2
parent[2] = 4
parent[4] = 1
parent[1] = 0

end = 5
start = 0

def recur_path(start, end, parent):
    if start == end:
        print(start)
    else:
        recur_path(start, parent[end], parent)
        print(end)
