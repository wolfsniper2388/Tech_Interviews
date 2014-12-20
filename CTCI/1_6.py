''' Rotate a matrix by 90 degrees clockwise in place
'''

def rotate_matrix (matrix):
    N = len(matrix)
    # start from the outside most layer and move inward
    # i.e. start from layer 0 to layer N/2-1
    for layer in range(N/2):
        # start: the first index of the top row of current layer
        start = layer
        # end: the last index of the top row of current layer
        end = N-1-layer
        # iterate from start to end-1 (NOT tO end)
        for i in range (start, end):
            # how far has i gone away from start
            offset=i-start
            top=matrix[start][i]
            # left -> top
            matrix[start][i]=matrix[end-offset][start]
            # bottom -> left
            matrix[end-offset][start]=matrix[end][end-offset]
            # right -> bottom
            matrix[end][end-offset]=matrix[i][end]
            # top -> right
            matrix[i][end]=top
    return matrix
    
if __name__=='__main__':
    matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    print matrix
    print rotate_matrix(matrix)
    
