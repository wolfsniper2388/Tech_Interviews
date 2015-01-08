'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
=[1,1,2], [1,2,1], and [2,1,1].

Note, the program should also cover the all-distinct situation
'''

from copy import deepcopy

def get_permutations_1(A):
    curr_result = []
    results = []
    visited = set([])
    get_permutations_helper(A, curr_result, results, visited, 0)
    return results

def get_permutations_helper(A, curr_result, results, visited, level):
    if level == len(A):
        results.append(deepcopy(curr_result))
        return
    
    for i in range(len(A)):
        if i not in visited:
            ''' The following two lines are not needed if A has all distinct numbers
            '''
            if i > 0 and A[i] == A[i-1] and i-1 not in visited:
                continue
            curr_result.append(A[i])
            visited.add(i)
            get_permutations_helper(A, curr_result, results, visited, level+1)
            curr_result.pop()
            visited.remove(i)
    return

def get_permutations_2(A):
    if len(A)==1:
            return [[A[0]]]
    prev_str = A[:-1]
    last_element = A[-1]
    prev_result=get_permutations_2(prev_str)
    new_result=[]
    for each_prev_permutation in prev_result:
        for position in range(len(each_prev_permutation)+1):
            # insert last_element in each position
            tmp_result = deepcopy(each_prev_permutation)
            tmp_result.insert(position, last_element)
            if tmp_result not in new_result:
                new_result.append(deepcopy(tmp_result))
    return new_result

if __name__=='__main__':
    test_cases = [[1,1],[2,3,4],[4,5,6,7], [1,1,2]]
    for each_test_case in test_cases:
        print 'approach 1', each_test_case, get_permutations_1(each_test_case)
        print 'approach 2', each_test_case, get_permutations_2(each_test_case)