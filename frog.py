def frog(A, D, X):
    mr = D
    map = [0]*X
    N = len(A)
    for i in range(N):
        if map[A[i]] == 0:
            map[A[i]] = 1
        if A[i] < mr:
            while canReach(A[i], D, map) != -1:
                A[i] += D
            mr = A[i]+D
        if mr >= X:
            return i
        
    return -1
                
def canReach(start, D, map):
    j = start + D
    while j % D != 0:
        if map[j] == 1:
            return j
        j -= 1
    return -1

if __name__ == '__main__':
    A = [1, 5, 9, 2, 7]
    D = 3
    X = 10
    print frog(A,D,X)