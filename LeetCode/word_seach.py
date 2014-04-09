''' Given a 2D board and a word, find if the word exists in the grid.
    The word can be constructed from letters of sequentially adjacent cell, 
    where "adjacent" cells are those horizontally or vertically neighboring. 
    The same letter cell may not be used more than once.
    E.g.
        Input:   board = [
                          'ABCE',
                          'SFCS',
                          'ADEE'
                         ]
                word = 'ABCCED' ---> True
                word = 'SEE'    ---> True
                word = 'ABCB'   ---> False
'''

def word_search(board, word):
    visited = set()
    for i in range(len(board)):
        for j in range((len(board[0]))):
            if board[i][j] == word[0]:
                if word_search_helper(board, i, j, word[1:], visited):
                    return True
                visited.clear()
    return False

def word_search_helper(board, i, j, word, visited):
    if not word:
        return True
    visited.add((i,j))
    # look right
    if j<len(board[0])-1 and board[i][j+1] == word[0] and (i,j+1) not in visited:
        if word_search_helper(board, i, j+1, word[1:], visited):
            return True
        visited.remove((i,j+1))
    
    # look up
    if i>0 and board[i-1][j] == word[0] and (i-1,j) not in visited:
        if word_search_helper(board, i-1, j, word[1:], visited):
            return True
        visited.remove((i-1,j))
        
    # look left
    if j>0 and board[i][j-1] == word[0] and (i,j-1) not in visited:
        if word_search_helper(board, i, j-1, word[1:], visited):
            return True
        visited.remove((i,j-1))
    
    # look down
    if i<len(board)-1 and board[i+1][j] == word[0] and (i+1,j) not in visited:
        if word_search_helper(board, i+1, j, word[1:], visited):
            return True
        visited.remove((i+1,j))
    return False


if __name__=='__main__':
    board = [
             'ABCE',
             'SFES',
             'ADEE'
            ]
    test_cases = ['ABCCED','SEE','ABCB', 'ABCESEEEFS']
    for each_test_case in test_cases:
        print each_test_case, word_search(board,each_test_case)
    board=['CAA',
           'AAA',
           'BCD'
           ]
    test_cases = ['AAB']
    for each_test_case in test_cases:
        print each_test_case, word_search(board,each_test_case)
    print word_search(['aa'],'aaa')