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
        
    Q.3
    
    Q.4
    
    
    
    
    
'''

from copy import deepcopy

def combo_sum_q1(A, target):
    results = []
    curr_result = []
    combo_sum_q1_helper(A, target, results, curr_result, 0)
    return results

def combo_sum_q1_helper(A, target, results, curr_result, curr_index):
    if target < 0:
        return
    if target == 0:
        results.append(deepcopy(curr_result))
        return
    for i in range(curr_index, len(A)):
        curr_result.append(A[i])
        combo_sum_q1_helper(A, target - A[i], results, curr_result, i)
        curr_result.pop()
    return




''' Q2
    suppose A=[1, 2,3,5,7] target =10
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

def combo_sum_q2(A, target):
    curr_result=[]
    results=[]
    combo_sum_q2_helper(A, target, results, curr_result, len(A)-1)
    return results

def combo_sum_q2_helper(A, target, results, curr_result, i):
    #if target<=0 or i==-1:
    #    return
    if i == -1:
        return
    
    if target == 0:
        #curr_result.append(A[i])
        if sorted(curr_result) not in results:
            results.append(deepcopy(sorted(curr_result)))
        #curr_result.pop()

    curr_result.append(A[i])
    combo_sum_q2_helper(A, target-A[i], results, curr_result, i-1)
    curr_result.pop()
    combo_sum_q2_helper(A, target, results, curr_result, i-1)
    curr_result.pop()

def combinationSum3(n,k):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        curr = []
        results = []
        dfs(n, k, curr, results, 1)
        return results
def dfs(n, k, curr, results, start):
    if k == 1:
        if n < 10:    
            curr.append(n)
            results.append(deepcopy(curr))
            curr.pop()
        return
    #a0 + a0+1 + a0+2 + ... + a0+k-1 <= n
    # a0 <= (n - k*(k-1)/2) / k
    end = (n - k*(k-1)/2) / k
    for i in range(start,end+1 if k > 2 else (n+1)/2):
        if i < 10:
            curr.append(i)
            dfs(n-i, k-1, curr, results, i+1)
            curr.pop()


if __name__=='__main__':
    '''
    print 'Q1'
    test_cases = [([2,3,5,6],10), ([7,3,5],10),([2],1), ([7,3,2],18)]
    for each_test_case in test_cases:
        A, target = each_test_case    
        print A, target, combo_sum_q1(A, target)
    print 'Q2'
    test_cases = [([1,1,2,5,6,7,10],8), ([10,1,2,7,6,1,5], 8),([7,3,2,6,5],10), ([2],1), ([3],3)]
    for each_test_case in test_cases:
        A, target = each_test_case
        print A, target, combo_sum_q2(A, target)
    '''    
    print 'Q3'
    test_cases = [(15,5),(6,2), (9,3)]
    for n,k in test_cases:
        print n,k, combinationSum3(n,k)
    