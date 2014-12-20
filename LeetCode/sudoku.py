''' Q1.
    Determine if a Sudoku is valid
        (1) Each row must have the numbers 1-9 occuring just once.
        (2) Each column must have the numbers 1-9 occuring just once.
        (3) And the numbers 1-9 must occur just once in each of the 9 sub-boxes of the grid.

    The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
    
    Q2.
    Write a program to solve a Sudoku puzzle by filling the empty cells.
    You may assume that there will be only one unique solution.
'''
from pprint import pprint


def is_valid_sudoku(board):
    rows = [[0 for j in range(9)] for i in range(9)]
    cols = [[0 for j in range(9)] for i in range(9)]
    ''' upper-left sub-box in board maps to blocks[0]
        upper-middle sub-box in board maps to blocks[1]
        upper-right sub-box in board maps to blocks[2]
        middle-left sub-box in board maps to blocks[3]
        middle-middle sub-box in board maps to blocks[4]
        middle-right sub-box in board maps to blocks[5]
        lower-left sub-box in board maps to blocks[6]
        lower-middle sub-box in board maps to blocks[7]
        lower-right sub-box in board maps to blocks[8]
        map function is 
        board[i][j] <=> blocks[i-i%3+j/3]
    '''
    blocks = [[0 for j in range(9)] for i in range(9)]
    
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                continue
            curr = int(board[i][j])-1
            if rows[i][curr] or cols[j][curr] or blocks[i-i%3+j/3][curr]:
                return False
            rows[i][curr] = cols[j][curr] = blocks[i-i%3+j/3][curr] = 1
    return True

def solve_sudoku(board):
    empty_pos = []
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                empty_pos.append((i,j))
    size = len(empty_pos)
    dfs(board, empty_pos, 0, size)
    
    
def is_valid(value, board, row, col):
    ''' check if board[row][col] == value is a valid
        it's valid only if:
            (1) there is no same value on the same row
            (2) there is no same value on the same column
            (3) there is no same value in the 3*3 sub-box
    '''
    for i in range(9):
        if board[row][i] == value or board[i][col] == value or board[row/3*3+i/3][col/3*3+i%3] == value:
            return False
    return True
            
    
    
def dfs(board, empty_pos, curr, size):
    if curr == size:
        return True
    
    row = empty_pos[curr][0]
    col = empty_pos[curr][1]
    # value = 1,2,...,9
    for value in range(1,10):
        # check before place
        if is_valid(str(value), board, row, col):
            board[row][col] = str(value)
            if dfs(board, empty_pos, curr+1, size):
                return True
            # else restore the board[row][col] to '.', and try next value
            board[row][col] = '.'
    # if all the values are not valid at board[row][col], this is invalid, so the value placed at empty_pos[curr-1] is also invalid
    return False

if __name__=='__main__':
    board = [ ['.','.','.','1','.','.','.','.','.'],
              ['.','7','.','.','2','.','8','1','.'],
              ['4','5','.','.','6','8','.','.','7'],
              ['.','1','8','.','.','.','.','7','.'],
              ['.','.','.','.','.','.','.','.','.'],
              ['.','4','9','.','.','.','5','3','.'],
              ['.','.','.','.','8','.','.','5','4'],
              ['.','3','7','.','1','.','.','2','.'],
              ['.','.','.','.','.','3','.','.','.']]
    print is_valid_sudoku(board)
    solve_sudoku(board)
    pprint(board)
    