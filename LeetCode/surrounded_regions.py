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
def get_neighbors(point,m,n):
    i = point[0]
    j = point[1]
    neighbors = []
    if j-1>=0:
        neighbors.append((i,j-1))
    if i-1>=0:
        neighbors.append((i-1,j))
    if j+1<=n-1:
        neighbors.append((i,j+1))
    if i+1<=m-1:
        neighbors.append((i+1,j))
    return neighbors
            
    

def go_chess(board): 
    if not board:
        return
    m = len(board)
    n = len(board[0])
    q = deque([])
    visited = set()
    
            
    #search for 'O' in the first row
    for j in range(n-1 if m>1 else n):
        if board[0][j] == 'O':
            board[0][j] = 'M'
            q.append((0,j))
            visited.add((0,j))
    #search for 'O' in the last column    
    for i in range(m-1):
        if board[i][n-1] == 'O':
            board[i][n-1] = 'M'
            q.append((i,n-1))
            visited.add((i,n-1))
    #search for 'O' in the last row
    for j in range(1,n):
        if board[m-1][j] == 'O':
            board[m-1][j] = 'M'
            q.append((m-1,j))
            visited.add((m-1,j))
    #search for 'O' in the first column    
    for i in range(1 if n>1 else 0,m):
        if board[i][0] == 'O':
            board[i][0] = 'M'
            q.append((i,0))
            visited.add((i,0))
            
    while q:
        curr_point = q.popleft()
        curr_row = curr_point[0]
        curr_col = curr_point[1]
        
        for each_neighbor in get_neighbors(curr_point,m,n):
            if board[each_neighbor[0]][each_neighbor[1]] == 'O' and each_neighbor not in visited:
                visited.add(each_neighbor)
                q.append(each_neighbor)
                board[each_neighbor[0]][each_neighbor[1]] = 'M'    # set to be Marked, which means alive or not to be flipped
    
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            if board[i][j] == 'M':
                board[i][j] = 'O'
        

if __name__=='__main__':
    board_chs=[]
    board_ch_1 = ['XOXXO',
                'XXOOX',
                'XXOOX',
                'XOOOX',
                'XXXXX']
    board_ch_2 = ['OXOO']
    board_ch_3 = ['O','O','X']
    board_chs.append(board_ch_1)
    board_chs.append(board_ch_2)
    board_chs.append(board_ch_3)
    
    for each_board_ch in board_chs:
        board = []
        for each_line in each_board_ch:
            board.append(list(each_line))
        pprint(board)
        print
        go_chess(board)
        pprint(board)
        print