''' Given a originally ascending sorted array of n integers that has been rotated an unknown number of times,
    write a method to find an element in the array
    E.g.
        Input: 5 and [9, 10, 1, 2, 5, 7]
        Output: 4 (the index of 5 is 4)
    
'''

def binary_search(A, target):
    low=0
    hight=len(A)
    mid=low+(high-low)/2
    if A[mid] == target:
        return mid
    elif A[mid] < target:
        low=mid+1
    else:
        high=mid-1
    return -1


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
    ''' A[mid] == A[start]
    else:
        if A[end] != A[mid]:
       '''     
       
       
if __name__=='__main__':
    print rotated_binary_search([12,15,1,3,5,7,10,11], 15, 0, 7)
    print rotated_binary_search([12,15,17,19,25,3,5], 3, 0, 6)
    print rotated_binary_search([1,1,1,3,4,1], 1, 0, 5)