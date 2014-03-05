''' Q1.
    Given number of rows, generate the first numRows of Pascal's triangle.
    E.g
        Input: 5
        Output: 
        [
         [1],
         [1,1],
         [1,2,1],
         [1,3,3,1],
         [1,4,6,4,1]
        ]
    Q2.
    Given an index k, return the kth row (0 based) of the Pascal's triangle.
    E.g.
        Input: 5
        Output: [1,5,10,10,5,1]
        Input: 3
        Output: [1,3,3,1]
'''

def generate_pascal_triangle(num_rows):
    if num_rows <= 0:
        return []
    triangle = [[1]]
    for i in range(1, num_rows):
        triangle.append([0] * (len(triangle[i-1])+1))
        triangle[i][0] = 1 
        triangle[i][-1] = 1 
        for j in range(1,len(triangle[i])-1):
            triangle[i][j] = triangle[i-1][j-1]+triangle[i-1][j]
    return triangle


def kth_pascal_triangle_row(k):
    row=[]
    
    for i in range(k+1):
        for j in range(i-1, 0, -1):
            row[j] = row[j-1]+row[j]
        row.append(1)
    
    '''
    # the following is also correct, but row.insert(0,1) will take O(i) time
    for i in range(k+1):
        row.insert(0, 1)
        for j in range(1,i):
            row[j] = row[j]+row[j+1]
    '''
    return row


if __name__=='__main__':
    
    test_cases = range(5)
    for each_test_case in test_cases:
        num_rows = each_test_case
        print 'Q1'
        print num_rows, generate_pascal_triangle(num_rows)
        
        k = each_test_case
        print 'Q2'
        print k, kth_pascal_triangle_row(k)