''' search a element in a 2D matrix where elements in rows and columns are both sorted in ascending order

    e.g
        Input: 100 and matrix:
                                   0  1  2  3   4   5   6   7   8   9
                                ---------------------------------------
                           0  |   15 20 40  85  100 130 140 150 160 175
                           1  |   17 35 80  95  110 135 145 155 165 190
                           2  |   30 55 95  105 120 160 172 187 195 200
                           3  |   40 80 100 120 130 175 180 190 200 210 
'''

class Coordinate:
    def __init__(self, row, col):
        self.row=row
        self.col=col
    def __repr__(self):
        return '%s%r' %(self.__class__.__name__, (self.row, self.col))

    # return True if self is at the upper left direction of point
    def is_upper_left(self, point):
        return self.row <= point.row and self.col <= point.col
    
    # return True if self's row and col is in the bound of matrix
    def is_in_bound(self, matrix):
        return self.row >=0 and self.col >= 0 and self.row < len(matrix) and self.col < len(matrix[0])
    
def get_mid(start, end):
    row_mid = start.row + (end.row-start.row)/2
    col_mid = start.col + (end.col-start.col)/2
    mid = Coordinate(row_mid, col_mid)
    return mid
    

def binary_search_matrix(matrix, target, start, end):
    if not start.is_in_bound(matrix) or not end.is_in_bound(matrix):
        return None
    if matrix[start.row][start.col] == target:
        return start
    if not start.is_upper_left(end):
        return None
    
    mid = get_mid(start, end)
    
    '''if we want to search for 100, the diagonal is [85, 110, 160, 180]
        diag_start = (0,3) : 85
        diag_end = (3,6) : 180
      '''
    diag_start = Coordinate(start.row, start.row+mid.col-mid.row)
    
    ''' if search for 210, there will be a bug if using the diag_end in the if block below
        the reason is diag_end will cross the bound diag_end= (3,10)
        so we check here, if diag_end cross the bound, diag_end.col will be end.col (else block)
    '''
    if end.row+mid.col-mid.row < end.col:
        diag_end= Coordinate(end.row, end.row+mid.col-mid.row)
    else:
        diag_end = Coordinate(end.col-(mid.col-mid.row), end.col)
    
    ''' binary search the quad section point
        find the first quad section coordinate which is larger than target
    '''
    while diag_start.is_upper_left(diag_end):
        diag_mid=get_mid(diag_start, diag_end)
        if target > matrix[diag_mid.row][diag_mid.col]:
            diag_start.row = diag_mid.row+1
            diag_start.col = diag_mid.col+1
        elif target < matrix[diag_mid.row][diag_mid.col]:
            diag_end.row = diag_mid.row-1
            diag_end.col = diag_mid.col-1
        # if what we are searching for is on the diagonal, then return this diag_mid 
        else:
            return diag_mid
    
    # after the loop, diag_start will be set to quad section coordinate
    quad_junc=diag_start
    
    # partition the matrix to lower left and upper right
    lower_left_start=Coordinate(quad_junc.row, start.col)
    lower_left_end=Coordinate(end.row, quad_junc.col-1)
    upper_right_start=Coordinate(start.row , quad_junc.col)
    upper_right_end=Coordinate(quad_junc.row-1, end.col)
    
    # search the lower left
    is_in_lower_left = binary_search_matrix(matrix, target, lower_left_start, lower_left_end)
    # if cannot find target in lower left, search upper right
    if not is_in_lower_left:
        return binary_search_matrix(matrix, target, upper_right_start, upper_right_end)
    return is_in_lower_left

if __name__=='__main__':
    matrix_num=[15,20,40,85,100,130,140,150,160,175,17,35,80,95,110,135,145,155,165,190,
                30,55,95,105,120,160,172,187,195,200,40,80,100,120,130,175,180,190,200,210]
    matrix=[[0 for col in range(10)] for row in range(4)]
    for row in range(4):
        for col in range(10):
            matrix[row][col]=matrix_num[row*10+col]
    print matrix
    
    #binary_search_matrix(matrix, 100, Coordinate(0,0), Coordinate(3,9))
    for i in matrix_num:
        print i,binary_search_matrix(matrix, i, Coordinate(0,0), Coordinate(3,9))
    
    