''' Given a sorted array of integers, find the starting and ending position of a given target value.
    Your algorithm's runtime complexity must be in the order of O(log n).
    If the target is not found in the array, return (-1, -1).
    E.g.
        Input: [5,7,7,8,8,10]
        Output: (3,4)
'''

def search_range(A, target):
    lower=0
    upper=len(A)
    while lower < upper:
        mid = lower+(upper-lower)/2
        if A[mid] < target:
            lower = mid+1
        else:
            upper = mid
            
    if A[lower] != target:
        return (-1,-1)
    start = lower
    lower=0
    upper = len(A)
    while lower < upper:
        mid = lower+(upper-lower)/2
        if A[mid] > target:
             upper = mid
        else:
            lower = mid+1
    end = upper-1
    return (start, end)


if __name__=='__main__':
    test_cases = [([8,8,8,8,8,8],8), ([2,8,8,8,8,8,8,8,8,9], 8), ([2,8,8,8,8,8,8,8,8,9], 2), ([2,8,8,8,8,8,8,8,8,9], 9),
                  ([1,3,4,4,5,6,7,7,7], 4),([2,3,7,8,8,8,9],8), ([1],1)]
    for each_test_case in test_cases:
        A, target = each_test_case
        print A, target, search_range(A, target)