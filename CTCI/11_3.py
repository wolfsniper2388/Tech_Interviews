''' Given a originally ascending sorted array of n integers that has been rotated an unknown number of times,
    write a method to find an element in the array
    E.g.
        Input: 5 and [9, 10, 1, 2, 5, 7]
        Output: 4 (the index of 5 is 4)    
'''

def rotated_binary_search(A, target, start, end):
    mid = start + (end-start)/2
    if A[mid]==target:
        return mid
    
    if start > end:
        return -1
    
    # left side is ordered
    if A[mid] > A[start]:
        if A[start] <= target <= A[mid]:
            return rotated_binary_search(A, target, start, mid-1)
        else:
            return rotated_binary_search(A, target, mid+1, end)
    # right side is orderd
    elif A[mid] <= A[start]:
        if A[mid] <= target <= A[end]:
            return rotated_binary_search(A, target, mid+1, end)
        else:
            return rotated_binary_search(A, target, start, mid-1)


''' find the pivot of rotation, same as find the index of minimum number in A
'''
def find_rotation_pivot(A):
    start=0;
    end=len(A)-1
    # A[start] > A[end] means A[start:end] is not sorted ascendingly
    while A[start]>A[end]:
        mid=start+(end-start)/2
        if A[mid]>A[end]:
            start=mid+1
        else:
            end=mid
    return start


if __name__=='__main__':
    test_cases=[([12,15,1,3,5,7,10,11], 3), ([12,15,17,19,25,3,5], 17), ([1,1,1,3,4,1], 3)]
    for each_test_case in test_cases:
        print 'test case', each_test_case
        print rotated_binary_search(each_test_case[0],each_test_case[1], 0, len(each_test_case[0]))
        print find_rotation_pivot(each_test_case[0])
    