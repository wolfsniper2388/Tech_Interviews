''' Given a m x n grid filled with non-negative numbers, 
    find a path from top left to bottom right which minimizes the sum of all numbers along its path.
    Note: You can only move either down or right at any point in time.
'''


''' Idea Dynamic Programming
    min_sum[i][j] = min (min_sum[i-1][j], min_sum[i][j-1]) + grid[i][i]
    Optimization:
        convert min_sum[i][j] to 1D array
    @param grid: the original grid
    @return: (min_sum, min_path), where min_sum is the sum of all the numbers is list min_path which is the path with 
             minimum sum
'''

import sys
def find_min_path_sun(grid):
    n_rows = len(grid)
    n_cols = len(grid[0])
    # 2D matrix that records the direction of the path, 0: coming from left, 1: coming from above
    direction = [[-1 for j in range(n_cols)] for i in range(n_rows)]
    min_sum = [sys.maxint]*n_cols
    min_sum[0]=0
    for i in range(n_rows):
        min_sum[0]+=grid[i][0]
        direction[i][0]=1
        for j in range(1, n_cols):
            if min_sum[j-1]<min_sum[j]:
                min_sum[j] = min_sum[j-1]+grid[i][j]
                direction[i][j] = 0
            else:
                min_sum[j] = min_sum[j]+grid[i][j]
                direction[i][j] = 1
            #min_sum[j] = min(min_sum[j-1], min_sum[j])+grid[i][j]
    min_path=[]
    i = n_rows-1
    j = n_cols-1
    while i>=0 and j>=0:
        min_path.append(grid[i][j])
        if direction[i][j] == 0:
            j-=1
        else:
            i-=1
    min_path.reverse()
    return (min_sum[-1], min_path)

if __name__=='__main__':
    M=3
    N=4
    data = [1,5,7,9,3,2,12,20,8,4,15,6]
    grid = [[0 for j in range(N) ] for i in range(M)]
    for i in range(M):
        for j in range(N):
            grid[i][j] = data[i*N+j]
    print grid
    min_sum, min_path = find_min_path_sun(grid)
    print min_sum, min_path