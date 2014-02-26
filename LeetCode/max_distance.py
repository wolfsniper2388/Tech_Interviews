''' Given an array A of integers, find the maximum of j-i subjected to the constraint of A[i] < A[j].
    E.g.
        Input: [34, 8, 10, 3, 2, 80, 30, 33, 1]
        Output: 6 (7-1)
        Input: [9, 2, 3, 4, 5, 6, 7, 8, 18, 0]
        Output: 8 (8-0)
'''

def max_index_diff(A):
    left_min=[None] * len(A)
    right_max = [None] * len(A)
    left_min[0] = A[0]
    right_max[-1] = A[-1]
    for i in range(1,len(A)):
        left_min[i] = min(A[i], left_min[i-1])
    for j in range(len(A)-2, -1, -1):
        right_max[j] = max(A[j], right_max[j+1])
    
    i=j=0
    max_diff=-1
    while i<len(A) and j<len(A):
        if left_min[i] < right_max[j]:
            max_diff = max(max_diff, j-i)
            j+=1
        else:
            i+=1
    return max_diff

if __name__=='__main__':
    test_cases = [[34, 8, 10, 3, 2, 80, 30, 33, 1], [9, 2, 3, 4, 5, 6, 7, 8, 18, 0],[1],[1,2]]
    for each_test_case in test_cases:
        print each_test_case, max_index_diff(each_test_case)