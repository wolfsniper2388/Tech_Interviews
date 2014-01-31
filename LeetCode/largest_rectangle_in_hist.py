''' 
    Q1. Largest Rectangle in Histogram 
    Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, 
    find the area of largest rectangle in the histogram.
    E.g
        Input: [6,1,5,4,4,5,1,6]
        Output: 16 (4*4=16)
        Input: [1,1,3,1,1,1]
        Output: 6 (1:6 = 6)
        
    Q2. maximal rectangle
    Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.
    E.g 
        Input: [ [0,0,0,1],
                 [0,1,1,0],
                 [1,1,1,0],
                 [0,1,0,0]
                ]
'''


def larget_rectangle_in_hist(A):
    i = 0
    max_area = 0
    stack = []
    # add a dummy element so that all the elements will be poped out, stack will always be empty at last
    A.append(0)
    while i < len(A):
        if not stack or A[i]>=A[stack[-1]]:
            stack.append(i)
            i+=1
        else:
            tmp = stack.pop()
            if not stack:
                max_area = max(max_area, A[tmp]*i)
            else:
                max_area = max(max_area, A[tmp] * (i-stack[-1]-1))
    
    return max_area


def maximal_rectangle(board):
    M = len(board)
    N = len(board[0])
    height = [[0 for j in range(N)] for i in range(M)]
    '''
        if board[i][j] is 0, height[i][j] is 0
        else height[i][j] is height[i-1][j]+1
        e.g.
        height will be [[0,0,0,1]
                        [0,1,1,0]
                        [1,2,2,0]
                        [0,3,0,0]
                        ]
    '''
    for i in range(M):
        for j in range(N):
            if board[i][j] == 0:
                height[i][j] = 0
            else:
                if i == 0:
                    height[i][j] = 1
                else:
                    height[i][j] = height[i-1][j]+1 
    max_area = 0
    # then for each row, call larget_rectangle_in_hist
    for i in range(M):
        max_area = max(max_area, larget_rectangle_in_hist(height[i]))
    return max_area
    
    
    
if __name__=='__main__':
    'Q1'
    test_cases = [[6,1,5,4,4,5,1,6], [1,1,3,1,1,1]]
    for each_test_case in test_cases:
        print each_test_case, larget_rectangle_in_hist(each_test_case)
    'Q2'
    test_case = [ [0,0,0,1],
                 [0,1,1,0],
                 [1,1,1,0],
                 [0,1,0,0]
                ]
    print test_case, maximal_rectangle(test_case)