''' Given a originally ascending sorted array of n integers that has been rotated an unknown number of times,
    write a method to find an element in the array with duplicates
    E.g.
        Input: 5 and [9, 10, 1, 2, 5, 7, 7, 7]
        Output: 4 (the index of 5 is 4)    
'''

def rotated_binary_search(A, target):
    start = 0
    end = len(A)-1
    
    while (start <= end):
        mid = start + (end-start)/2
        if A[mid]==target:
            return mid
        # left side is ordered
        if A[mid] > A[start]:
            if A[start] <= target <= A[mid]:
                end = mid-1
            else:
                start = mid+1
                # right side is ordered
        elif A[mid] < A[start]:
            if A[mid] <= target <= A[end]:
                start = mid+1
            else:
                end = mid-1
        else:
            start+=1
    return False

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
    test_cases=[([12,15,1,3,5,7,10,11], 3), ([12,15,17,19,25,3,5], 17), ([2, 2, 2, 1, 2, 2, 2, 2, 2 ], 1)]
    for each_test_case in test_cases:
        print 'test case', each_test_case
        print rotated_binary_search(each_test_case[0],each_test_case[1])
        print find_rotation_pivot(each_test_case[0])
    