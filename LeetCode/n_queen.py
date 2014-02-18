''' Q1.
    The n-queens puzzle is the problem of placing n queens on an n*n chess board such that no two queens attack each other.
    Given an integer n, return all distinct solutions to the n-queens puzzle.
    Q2.
    Now, instead outputting board configurations, return the total number of distinct solutions.
'''
from copy import deepcopy
def n_queens_solver(N):
    results=[]
    curr_result = [-1 for i in range(N)]
    dfs( 0, N, curr_result, results)
    print results
    
def is_valid(curr_result, curr_row, col, N):
    'check if curr_result[curr_row] == col is valid'
    for i in range(curr_row):
        # same column or on 45 diagonal or on 135 diagonal
        if col == curr_result[i] or col == curr_result[i]-(curr_row-i) or col == curr_result[i]+(curr_row-i):
            return False
    return True 
    
def dfs(curr_row, N, curr_result, results):
    if curr_row == N:
        results.append(deepcopy(curr_result))
    else:
        # for each possible position on curr_row
        for col in range(N):
            if is_valid(curr_result, curr_row, col, N):
                curr_result[curr_row] = col
                dfs(curr_row+1, N, curr_result, results)


if __name__=='__main__':
    n_queens_solver(4)