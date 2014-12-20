''' There are two sorted arrays A and B of size m and n respectively. 
    Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
    median is defined to be the middle one if sorted array length is odd
                            the mean of the middle two numbers if sorted array length is even
'''

import sys
'''
find the kth smallest (1 based) element in the union of two sorted arrays A and B
'''
def find_kth_smallest(A, B, k):
        m = len(A)
        n = len(B)
        #assert (k <= m +n and k > 0)
        #i = k/2
        #j = k-i-1
        i = int ((m/float((m+n))) * (k-1))
        j = k-1-i   #(i+j = k-1)
        
        Ai_prev = A[i-1] if i>0 else -sys.maxint
        Bj_prev = B[j-1] if j>0 else -sys.maxint
        Ai = A[i] if i<m else sys.maxint
        Bj = B[j] if j<n else sys.maxint
        
        if Ai == Bj:
            return Ai
        
        if Bj_prev < Ai < Bj:
            return Ai
        elif Ai_prev < Bj < Ai:
            return Bj
        
        if Ai < Bj:
            # exclude A's lower part and B's upper part
            # exclude A's lower part => k = k-i-1
            return find_kth_smallest(A[i+1:], B[:j+1], k-i-1)
        else:   # Ai > Bj
            # exclude B's lower part and A's upper part
            # exclude B's lower part => k = k-j-1
            return find_kth_smallest(A[:i+1], B[j+1:], k-j-1)
            
def find_median (A, B):
    assert (A or B)
    total_len = len(A) + len(B)
    if total_len % 2 == 1:
        return find_kth_smallest(A, B, (total_len+1)/2)
    else:
        return (find_kth_smallest(A, B, (total_len)/2) + find_kth_smallest(A, B, total_len/2 + 1) ) /2.0
        
if __name__=='__main__':
    test_cases = [([1,5,8,13,15,18,21], [2,7,14]), ([1,2],[1,2]), ([],[1]), ([], [])]
    for each_test_case in test_cases:
        A, B = each_test_case
        #print find_kth_smallest(A, B, 3)
        print find_median(A, B)
        