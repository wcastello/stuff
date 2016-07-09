from collections import deque
import sys

def idx(c):
    return ord(c)-48

class Node:
    def __init__(self, data=None, depth=0):
        self.data = data
        self.depth = depth
        self.children = 75*[None]

class Trie:
    def __init__(self):
        self.root = Node('', 0)

    def insert(self, word):
        self.insert_(self.root, word, 0)

    def insert_(self, root, word, k):
        if k == len(word)-1:
            root.children[idx(word[k])] = Node('*', k)
            return

        cidx = idx(word[k])

        if not root.children[cidx]:
            root.children[cidx] = Node(word[k], k+1)

        self.insert_(root.children[cidx], word, k+1)

def read_insert_words(f, trie):
    for word in f:
        trie.insert(word.strip())

def read_boggle_into(n, table):
    table.append((n+2)*[None])
    for i in range(n):
        table.append([None] + list(input()) + [None])
    table.append((n+2)*[None])

def find_all_words_starting_at(boggle, start, seen, trieroot, length):
    """ Find all starting at boggle[i][j], with start = (i, j) that have
        at least 3 characters.
        Return a list of words (may include repeated words from different paths)
    """
    i, j = start
    suffixes = []

    if trieroot.data == '*' and length >= 3:
        suffixes = ['']

    prefix = boggle[i][j]
    neighboors = get_neighboors(boggle, i, j)
    for neighboor in neighboors:
        i_, j_ = neighboor
        if boggle[i_][j_] not in seen and trieroot.children[idx(boggle[i_][j_])]:
            seen_ = seen.union({boggle[i_][j_]})
            suffixes += find_all_words_starting_at(boggle, (i_, j_), seen_,
                trieroot.children[idx(boggle[i_][j_])], length+1)

    words = []
    for suffix in suffixes:
        words.append(prefix + suffix)
    return words


def get_neighboors(boggle, i, j):
    neighboors = []
    for i_ in range(i-1, i+2):
        for j_ in range(j-1, j+2):
            if boggle[i_][j_] and (i_ != i or j_ != j): neighboors.append((i_, j_))
    return neighboors

def main(argv):
    trie = Trie()
    n = int(input())
    with open(argv[1], 'r') as f:
        read_insert_words(f, trie)

    boggle = []
    read_boggle_into(n, boggle)

    words = []
    for i in range(1, len(boggle)-1):
        for j in range(1, len(boggle)-1):
            words += find_all_words_starting_at(boggle, (i, j), {boggle[i][j]},
                trie.root.children[idx(boggle[i][j])], 0)

    print(', '.join(sorted(set(words), key=lambda s: len(s))))

if __name__ == '__main__':
    main(sys.argv)
