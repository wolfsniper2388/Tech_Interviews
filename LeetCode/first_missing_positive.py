''' Given an unsorted integer array, find the first missing positive integer.
    E.g.  
        Input: [1,2,0]
        Output: 3
        Input: [3,5,-1,1]
        Output: 2
        Input: [5,6,7,9]
        Output: 1
    The algorithm should run in O(n) time and uses constant space.
''' 

def find_first_missing_positive(A):
    i=0
    n = len(A)
    while i < n:
        if 0<A[i]<n and A[i]-1 != i and A[A[i]-1]!=A[i]:
            tmp = A[A[i]-1]
            A[A[i]-1] = A[i]
            A[i] = tmp
        else:
            i+=1
    for i in range(n):
        if A[i]!=i+1:
            return i+1
    return n+1

if __name__=='__main__':
    test_cases=[[1,2,0],[3,5,-1,1],[5,6,7,9],[2,1]]
    for each_test_case in test_cases:
        print each_test_case, find_first_missing_positive(each_test_case)