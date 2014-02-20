''' update M to N from bit i to bit j (bit i means the ith bit in num counting from right)
    E.g.
        Input: N = 1000000, M = 1010, i = 2, j = 5
        Output: N = 1101000
'''

def multi_update(n,m,i,j):
    print n
    left = ~((1 << (j+1)) -1)  # left = 1110000000
    right = (1<<i) -1   # right = 000000011
    two_sides_mask = left | right
    middle_mask = m<<i
    n_cleared = n & two_sides_mask
    return bin(n_cleared | middle_mask)
    
if __name__=='__main__':
    N = 0b101100000
    M = 0b0110
    i=2
    j=5
    print multi_update(N,M,i,j)