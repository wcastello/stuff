def rotate_90(matrix, n):
    """ Rotate NxN matrix by 90 degrees.
        Return the rotated matrix.
        O(n^2) in time, O(1) in space
    """
    transpose(matrix, n)
    for i in range(n):
        # reverse_row(matrix[i], n)
        matrix[i].reverse()

def transpose(matrix, n):
    for i in range(0, n):
        for j in range(i+1, n):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = tmp

def reverse_row(row, n):
    for i in range(n//2):
        tmp = row[i]
        row[i] = row[n-1-i]
        row[n-1-i] = tmp