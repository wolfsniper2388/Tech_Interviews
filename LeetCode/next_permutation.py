''' Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
    If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
    The replacement must be in-place, do not allocate extra memory.
    E.g.
        Input: [9,5,1]
        Output: [1,5,9]
        Input: [3,5,9,6,4]
        Output: [3,6,4,5,9] 
'''

''' Algorithm: 
        1. Find the largest index i such that a[i] < a[i + 1]. If no such index exists, the permutation is the last permutation.
        2. Find the largest index j such that a[i] < a[j].
        3. Swap the value of a[i] with that of a[j].
        4. Reverse the sequence from a[i + 1] up to and including the final element a[n].
'''

def next_permutation(A):
    i = len(A)-1
    while i > 0:
        if A[i] > A[i-1]:
            break
        else:
            i-=1
    if i==0:
        return sorted(A)
    i-=1
    j = len(A)-1
    while j > i:
        if A[j] > A[i]:
            break
        else:
            j-=1
    A[i],A[j] = A[j], A[i]
    return A[:i+1]+sorted(A[i+1:])

if __name__=='__main__':
    test_cases = [[1,2,3], [4,3,1], [3,5,9,6,4], [3,6,8,2]]
    for each_test_case in test_cases:
        print each_test_case, next_permutation(each_test_case)
    
            