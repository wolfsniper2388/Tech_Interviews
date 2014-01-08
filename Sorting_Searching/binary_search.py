def binary_search(A, target):
    low=0
    high=len(A)-1
    while low <= high:
        mid=low+(high-low)/2
        if A[mid] == target:
            return mid
        elif A[mid] < target:
            low=mid+1
        else:
            high=mid-1
    return -1

if __name__=='__main__':
    print binary_search([1,3,5,7,9,11,13], 11)