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


# spirally print each layer
def print_layer_spiral(matrix, layer, M, N):
    for j in range(layer, N-1-layer):
        print matrix[layer][j],
    for i in range(layer,M-1-layer):
        print matrix[i][N-1-layer],
    for j in range(N-1-layer, layer, -1):
        print matrix[M-1-layer][j],
    for i in range(M-1-layer, layer, -1):
        print matrix[i][layer],


# for each layer, call print_layer_spiral to spirally print each layer
# starts from the most outside layer 0, and move inward
def print_matrix_spiral(matrix, M, N):
    for layer in range((M+1)/2):
        print_layer_spiral(matrix, layer, M, N)


if __name__=='__main__':
    data=[x for x in range(1,31)]
    M=5
    N=6
    matrix=[[0 for j in range(N)] for i in range(M)]
    
    for i in range(M):
        for j in range(N):
            matrix[i][j] = data[i*6+j]
    print 'level printing'
    print matrix
    
    print 'spiral printing'
    print_matrix_spiral(matrix, M, N)