'''  find subset of elements that are selected from a given set whose sum adds up to a given number K
''' 

from copy import deepcopy

def subset_sum_helper(A, results, curr_result, curr_sum, index, target):
    if curr_sum == target:
        if curr_result not in results:
            results.append(deepcopy(curr_result))
    else:
        for i in range(index, len(A)):
            curr_result.append(A[i])
            subset_sum_helper(A, results, curr_result, curr_sum+A[i], i+1 ,target)
            curr_result.pop()
    
    
    
    
def subset_sum(A, target):
    results=[]
    curr_result=[]
    subset_sum_helper(A, results, curr_result, 0, 0, target)
    return results

if __name__=='__main__':
    test_cases=[([3,5,2], 5),([5,3,1,7,2],10), ([2,2,2,2,2],8), ([2,1,4,3],20)]
    for each_test_case in test_cases:
        A,target = each_test_case
        print A, target, subset_sum(A,target)