'''Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
'''


def setZeroes(self, matrix):
    m = len(matrix)
    n = len(matrix[0])
    first_row_zero = False
    first_col_zero = False
    for i in range(m):
        if matrix[i][0] == 0:
                first_col_zero = True
    for j in range(n):
        if matrix[0][j] == 0:
            first_row_zero = True
        
    for i in range(1,m):
        for j in range(1,n):
            if matrix[i][j] == 0:
                matrix[i][0] = matrix[0][j] = 0
        
    for i in range(1,m):
        for j in range(1,n):
            if matrix[i][0] ==0 or  matrix[0][j] == 0:
                matrix[i][j] = 0
    if first_row_zero:
        for j in range(n):
            matrix[0][j] = 0
    if first_col_zero:
        for i in range(m):
            matrix[i][0] = 0