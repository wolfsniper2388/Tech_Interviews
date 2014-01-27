''' The set [1,2,3,...,n] contains a total of n! unique permutations.
    By listing and labeling all of the permutations in order,    
    We get the following sequence (ie, for n = 3):
    "123"    
    "132"
    "213"
    "231"
    "312"
    "321"
    Given n and k, return the kth permutation sequence. (k is 0 based)
    E.g
    Input: n=4, k=10
    Output: '2413'
'''
import math
def find_kth_permutation(n,k):
    if k >= math.factorial(n):
        return None
    result_ch_list = find_kth_permutation_helper(range(1,n+1), k, [])
    return ''.join(result_ch_list)

def find_kth_permutation_helper(A, k, ch_list):
    n = len(A)
    if n == 1:
        ch_list.append(str(A[0]))
        return ch_list
    digit = A[k/(math.factorial(n-1))]
    ch_list.append(str(digit))
    A.remove(digit)
    find_kth_permutation_helper(A, k % (math.factorial(n-1)), ch_list)
    return ch_list
    
if __name__=='__main__':
    test_cases = [(4,10), (1,2), (3,0), (3,5)]
    for each_test_case in test_cases:
        n,k=each_test_case
        print each_test_case, find_kth_permutation(n,k)