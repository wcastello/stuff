def BSTSeqs(root):
    if not root:
        seqs = [[]]
    elif not root.left and not root.right:
        seqs = [[root.data]]
    else:
        seqs = []
        lseqs = BSTSeqs(root.left)
        rseqs = BSTSeqs(root.right)
        for lseq in lseqs:
            for rseq in rseqs:
                print('rseq=', rseq, 'lseq=', lseq)
                for merge in all_merges(lseq, rseq):
                    seqs.append([root.data] + merge)
    return seqs

def printBSTSeqs(seqs):
    print(', '.join(str(seq) for seq in seqs))

# weaves, interleaves, merges, whatever you call it
def all_merges(a, b):
    if not a and not b:
        merges = [[]]
    elif not b:
        merges = [a]
    elif not a:
        merges = [b]
    else:
        merges = []
        for merge in all_merges(a[1:], b):
            merges.append([a[0]] + merge)
        for merge in all_merges(a, b[1:]):
            merges.append([b[0]] + merge)
    return merges
