def setrowzero(matrix, m, n):
    """ Set the entire row of an element to 0 if the element is 0
        O(m*n^2)(?) in time
    """
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                matrix[i] = n * [0]
                break

def setrowcolzero(matrix, m, n):
    """ Set the entire row and column of an element to 0's if the element
        is 0.
        O(m*n) in time
    """
    first_col_has_zero = False
    first_row_has_zero = False
    for x in matrix[0]:
        if x == 0:
            first_row_has_zero = True
            break

    for row in matrix:
        if row[0] == 0:
            first_col_has_zero = True
            break

    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0

    for i in range(m):
        if matrix[i][0] == 0:
            nullify_row(matrix, m, i)

    for j in range(n):
        if matrix[0][j] == 0:
            nullify_col(matrix, n, j)

    if first_row_has_zero:
        nullify_row(matrix, m, 0)

    if first_col_has_zero:
        nullify_col(matrix, n, 0)

def nullify_row(matrix, m, row):
    matrix[row] = [0] * m

def nullify_col(matrix, n, col):
    for i in range(n):
        matrix[i][col] = 0
