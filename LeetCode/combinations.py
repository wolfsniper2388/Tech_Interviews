''' Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
    E.g
        Input: n=4, k=2
        Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
'''
from copy import deepcopy
def combinations(n,k):
    if k<=0 or k > n:
        return
    A = range(1,n+1)
    return combination_helper(A, k, [], [], 0)

def combination_helper(A, k, curr_combo, result_combos, curr_index):
    if len(curr_combo) == k:
        result_combos.append(deepcopy(curr_combo))
        return result_combos
    while curr_index < len(A):
        curr_combo.append(A[curr_index])
        combination_helper(A, k , curr_combo, result_combos, curr_index+1)
        curr_combo.pop()
        curr_index+=1
    return result_combos

if __name__=='__main__':
    test_cases = [(4,2),(3,1),(5,3),(4,4)]
    for each_test_case in test_cases:
        n,k = each_test_case
        print n,k,combinations(n,k)