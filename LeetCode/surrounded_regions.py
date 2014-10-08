'''
Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
'''

from collections import deque
from pprint import pprint

''' return a list of neighbors' points of @param point
'''
def get_neighbors(point):
    i = point[0]
    j = point[1]
    neighbors = []
    if j-1>=0:
        neigbors.extend([(i,j-1),(i-1,j-1)])

def go_chess(board): 
    m = len(board)
    n = len(board[0])
    q = deque([])
    visited = set()
    #search for 'O' in the first row
    for j in range(n-1):
        if board[0][j] == 'O':
            q.append((0,j))
            visited.add((0,j))
    #search for 'O' in the last column    
    for i in range(m-1):
        if board[i][n-1] == 'O':
            q.append((i,n-1))
            visited.add((i,n-1))
    #search for 'O' in the last row
    for j in range(1,n):
        if board[m-1][j] == 'O':
            q.append((m-1,j))
            visited.add((m-1,j))
    #search for 'O' in the first column    
    for i in range(1,m):
        if board[i][0] == 'O':
            q.append((i,0))
            visited.add((i,0))
            
    while q:
        curr_point = q.popleft()
        curr_row = curr_point[0]
        curr_col = curr_point[1]
        if curr_point not in visited:
            q.append(curr_point)
            visited.add(curr_point)
        
        
        
        

if __name__=='__main__':
    board_ch = ['XOXXO',
                'XOOOX',
                'XXOOX',
                'OOOOX',
                'XXXXX']
    board = []
    for each_line in board_ch:
        board.append(list(each_line))
    pprint(board)
    
    go_chess(board)