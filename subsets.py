'''
Given a set of integers, A, return all possible subsets.

Note:
A can contain duplicates
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
e.g.
    Input: [1,2,3]

    Output: [[3], [1], [2], [1,2,3], [1,3], [2,3], [1,2], [] ]
    
    Input: [2,1,2]
    
    Output: [[], [1,2,2], [1], [2], [1,2], [2,2]]
'''

from copy import deepcopy
def get_subsets(A):
    curr_result = []
    results = []
    A = sorted(A)
    get_subsets_helper(A, curr_result, results, 0)
    results.append([])
    return results

def get_subsets_helper(A, curr_result, results, curr_index):
    if curr_index == len(A):
        return
    
    i = curr_index
    while i < len(A):
        curr_result.append(A[i])
        results.append(deepcopy(curr_result))
        get_subsets_helper(A, curr_result, results, i+1)
        curr_result.pop()
        ''' The following two lines are not needed when A has all distinct numbers
        '''
        while i < len(A)-1 and A[i] == A[i+1]:
            i+=1
        i+=1    
        
if __name__=='__main__':
    test_cases = [[1,2,3], [2,5], [6], [5,2,5]]
    for each_test_case in test_cases:
        print each_test_case, get_subsets(each_test_case)