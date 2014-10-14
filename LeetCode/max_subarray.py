''' Find the contiguous sub-array within an array (containing at least one number) which has the largest sum.
    E.g.
        Input: [-2,1,-3,4,-1,2,1,-5,4]
        Output: ([4, -1, 2, 1], 6)
'''


import sys
def max_sum_subarray_divide_and_conquer_helper(A, start, end):
    if start>=end:
        return A[start]
    mid = start+(end-start)/2
    left_max_sum_ret = max_sum_subarray_divide_and_conquer_helper(A, start, mid-1)
    right_max_sum_ret = max_sum_subarray_divide_and_conquer_helper(A, mid+1,end)
    left_max_sum = -sys.maxint
    right_max_sum = -sys.maxint
    sum=0
    for i in range(mid, start-1, -1):
        sum+=A[i]
        if sum > left_max_sum:
            left_max_sum = sum
    sum=0
    for i in range(mid+1, end+1):
        sum+=A[i]
        if sum > right_max_sum:
            right_max_sum = sum
    return max(left_max_sum+right_max_sum, left_max_sum_ret, right_max_sum_ret)
        
    


def max_sum_subarray_divide_and_conquer(A):
    return max_sum_subarray_divide_and_conquer_helper(A, 0, len(A)-1)
    

''' Algorithm:
        maintain three pointers: curr, start, end, which record the curr position, the position of the
        current max subarray start and the position of the current max subarray end
        iterate through A, curr++
        if A[curr] > curr_sum then update sum, start, end, this means the previous sum is less than current value,
        so the previous curr_sum is not optimal
        if sum > max_sum then update the end to curr and update max_sun to curr_sum
    @return: a tuple consisting of the subarray with max sum and the curr_sum
'''
def find_max_subarray(A):
    curr=start=end=max_sum=curr_sum=0
    while curr < len(A):
        curr_sum += A[curr]
        if A[curr] > curr_sum:
            start=end=curr
            curr_sum = A[curr]
        if curr_sum > max_sum:
            max_sum = curr_sum
            end = curr
        curr+=1
        
    return (A[start: end+1], max_sum)

if __name__=='__main__':
    test_cases = [[1], [-2,1,-3,4,-1,2,1,-5,4], [4,1,2,3], [1,-2,3,10,-4,7,2,-5]]
    for each_test_case in test_cases:
        print each_test_case, find_max_subarray(each_test_case)
        print max_sum_subarray_divide_and_conquer(each_test_case)

