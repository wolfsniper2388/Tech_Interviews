''' Q.1
    Given a collection of candidate numbers (C) and a target number (T), 
    find all unique combinations in C where the candidate numbers sums to T.
    Each number in C may be used unlimited times in the combination.
    Note:
        All numbers (including target) will be positive integers.
        Elements in a combination must be in non-descending order. 
        The solution set must not contain duplicate combinations.
    E,g.
        Input: [2,3,5,6], target=10
        Output: [[2,2,2,2,2], [2,2,2,3,3], [2,2,6], [2,3,5], [5,5]]
        
    Q.2 
    Given a collection of candidate numbers (C) and a target number (T), 
    find all unique combinations in C where the candidate numbers sums to T.
    Each number in C may only be used once in the combination.
    Note:
        All numbers (including target) will be positive integers.
        Elements in a combination must be in non-descending order. 
        The solution set must not contain duplicate combinations.
    E.g 
        Input: [1,1,2,5,6,7], target=8
        Output: [[1,7], [1,2,5], [2,6], [1,1,6]
'''

from copy import deepcopy

def combo_sum_q1_helper(A, target, results, curr_result, curr_index):
    if target < 0:
        return
    if target == 0:
        results.append(deepcopy(curr_result))
        return results
    for i in range(curr_index, len(A)):
        curr_result.append(A[i])
        combo_sum_q1_helper(A, target - A[i], results, curr_result, i)
        curr_result.pop()
    return results


''' suppose A=[1, 2,3,5,7] target =10
    one recursion tree path is:
                        10, 7
                    /         \
                 3,5          10,5
                 / \          /   \      
             -1,3  3,3       5,3   10,3  
                   / \       / \
                 0,2  3,2   2,2 5,2
                      / \
                    1,1  3,1
                       
'''          
def combo_sum_q2_helper(A, target, results, curr_result, i):
    if target<=0 or i==-1:
        return None
    
    if target == A[i]:
        curr_result.append(A[i])
        if sorted(curr_result) not in results:
            results.append(deepcopy(sorted(curr_result)))
        curr_result.pop()

    curr_result.append(A[i])
    combo_sum_q2_helper(A, target-A[i], results, curr_result, i-1)
    curr_result.pop()
    combo_sum_q2_helper(A, target, results, curr_result, i-1)

def combo_sum_q2(A, target):
    curr_result=[]
    results=[]
    combo_sum_q2_helper(A, target, results, curr_result, len(A)-1)
    return results

if __name__=='__main__':
    print 'Q1'
    test_cases = [([2,3,5,6],10), ([7,3,5],10),([2],1), ([7,3,2],18)]
    for each_test_case in test_cases:
        A, target = each_test_case    
        print A, target, combo_sum_q1_helper(A, target, [], [], 0)
    print 'Q2'
    test_cases = [([1,1,2,5,6,7,10],8), ([10,1,2,7,6,1,5], 8),([7,3,2,6,5],10), ([2],1), ([3],3)]
    for each_test_case in test_cases:
        A, target = each_test_case
        print A, target, combo_sum_q2(A, target)
    