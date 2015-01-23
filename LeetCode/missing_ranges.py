'''
Given a sorted integer array where the range of elements are [lower, upper] inclusive, return its missing ranges.

For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].
'''

def missing_ranges(A, lower, upper):
    if not A:
        return [str(lower)+'->'+str(upper)] if lower != upper else [str(lower)]
    prev = 0
    result = []
    n = len(A)
    # deal with middle
    for curr in range(1, n):
        if A[curr] - A[prev] > 2:
            result.append(str(A[prev]+1) + '->' + str(A[curr]-1))
        elif A[curr] - A[prev] == 2:
            result.append(str(A[curr]-1))
        prev = curr
    # deal with lower to A[0]
    if A[0] - lower > 1:
        result.insert(0, str(lower) + '->' + str(A[0]-1))
    elif A[0] - lower == 1:
        result.insert(0, str(lower))
    # deal with A[n-1] to upper
    if upper - A[-1] > 1:
        result.append(str(A[n-1]+1) + '->' + str(upper))
    elif upper - A[-1] == 1:
        result.append(str(upper))
    
    return result

if __name__=='__main__':
    test_cases = [([1,2,3,4,5], 1, 5), ([0,1,3, 8], 0, 10), ([0,2,4,9],0,10), ([2,3,5,9], 0, 10), ([1,3,9], 0, 10), ([],1,1)]
    for each_test_case in test_cases:
        A, lower, upper = each_test_case
        print A, lower, upper, missing_ranges(A, lower, upper)
            
            
            