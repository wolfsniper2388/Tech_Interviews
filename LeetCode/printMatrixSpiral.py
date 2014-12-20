''' print a M*N matrix spirally
    E.g
        Input:  1 2 3
                4 5 6
                7 8 9
        Output: 1 2 3 6 9 8 7 4 5
        
        Input: 1  2  3  4
               5  6  7  8
               9  10 11 12
        Output: 1 2 3 4 8 12 11 10 9 5 6 7
'''

# for each layer, call print_layer_spiral to spirally print each layer
# starts from the most outside layer 0, and move inward
def print_spiral_matrix(matrix):
    if not matrix:
        return []
    begin_row = 0;
    end_row = len(matrix)-1
    begin_col = 0
    end_col = len(matrix[0])-1 
    result = []
    while 1:
        for j in range(begin_col, end_col+1):
            result.append(matrix[begin_row][j])
        begin_row+=1
        if begin_row > end_row:
            break
        for i in range(begin_row, end_row+1):
            result.append(matrix[i][end_col])
        end_col-=1
        if begin_col > end_col:
            break
        for j in range(end_col, begin_col-1, -1):
            result.append(matrix[end_row][j])
        end_row-=1
        if begin_row > end_row:
            break
        for i in range(end_row, begin_row-1, -1):
            result.append(matrix[i][begin_col])
        begin_col+=1
        if begin_col > end_col:
            break
    return result

def generate_spiral_matrix(n):
    result = [[0 for i in range(n)] for j in range(n)]
    num = 1
    begin_row = 0
    end_row = n-1;
    begin_col = 0
    end_col = n-1;
    while begin_row <= end_row:
        for i in range(begin_col, end_col+1):
            result[begin_row][i] = num
            num += 1
        begin_row += 1
            
        for i in range(begin_row, end_row+1):
            result[i][end_col] = num
            num += 1
        end_col -= 1
            
        for i in range(end_col, begin_col-1, -1):
            result[end_row][i] = num
            num += 1
        end_row -= 1
            
        for i in range(end_row, begin_row-1, -1):
            result[i][begin_col] = num
            num += 1
        begin_col += 1
        
    return result;


if __name__=='__main__':
    test_cases = [[[1,2,3],[4,5,6],[7,8,9]],[[1]], [[1,2,3,4,5]]]
    for matrix in test_cases:
        print
        print 'level printing'  
        print matrix
    
        print 'spiral printing'
        print print_spiral_matrix(matrix)
    print 'Test generate_spiral_matrix'
    for i in range(4):
        print generate_spiral_matrix(i)