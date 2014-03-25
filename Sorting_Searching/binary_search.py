''' binary search a target in A, if target not in A, then return the position it can be inserted into A 
'''

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
    return low

if __name__=='__main__':
    test_array = [1,3,5,7,9,11,13]
    for each_target in range(15):
        print each_target, binary_search(test_array, each_target)