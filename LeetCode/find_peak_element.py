'''
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] != num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -INF.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
'''

def find_peak_element(A):
    low = 0
    high = len(A)-1
    if high == 0:
        return 0
        
    while low <= high:
        mid = low + (high-low)/2
        if mid == 0 and A[0] > A[1]:
            return 0
        elif mid == len(A)-1 and A[-1] > A[-2]:
            return len(A)-1
        elif A[mid] > A[mid-1] and A[mid] > A[mid+1]:
            return mid
        elif A[mid-1] < A[mid] < A[mid+1]:
            low = mid+1
        elif A[mid-1] > A[mid] > A[mid+1]:
            high = mid-1
        else:
            low = mid + 1
    
        
    #return find_peak_element_helper(A, 0, len(A)-1)

#def find_peak_element_helper(A, low, high):
    
if __name__=='__main__':
    test_cases = [[5,3,7,9,15,2], [1,2,3,5], [5,4,3,1],[3], [2,1], [1,6], [1,3,6,4,8,9,7], [3,4,3,2,1]]
    for each_test_case in test_cases:
        print each_test_case, find_peak_element(each_test_case)