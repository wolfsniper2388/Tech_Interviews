''' A magic index in an array A[0...n-1] is defined to be an index such that A[i]=i
    Q1 Given a sorted array of distinct integers, write a method to find a magic index in array A, if one exists
    Q2 what if the values are not distinct
'''

''' Q1
'''

def find_magic_index_distinct(A,start, end):
    if start>end:
        return
    mid=start+(end-start)/2
    if A[mid]>mid:
        find_magic_index_distinct(A, start, mid-1)
    elif A[mid]<mid:
        find_magic_index_distinct(A, mid+1, end)
    else:
        find_magic_index_distinct.result.append(mid)
        find_magic_index_distinct(A, start, mid-1)
        find_magic_index_distinct(A, mid+1, end)
        
find_magic_index_distinct.result = []



''' Q2
'''

def find_magic_index_nondistinct(A, start, end):
    if start>end:
        return
    mid=start+(end-start)/2
    if A[mid]>mid:
        # search left side as usual, but for right side, can skip some elements
        find_magic_index_nondistinct(A, start, mid-1)
        find_magic_index_nondistinct(A, max(mid+1,A[mid]), end)
    elif A[mid]<mid:
        # search right side as usual, but for left side, can skip some elements
        find_magic_index_nondistinct(A, start, min(mid-1, A[mid]))
        find_magic_index_nondistinct(A, mid+1, end)
    else:
        find_magic_index_nondistinct.result.append(mid)
        find_magic_index_nondistinct(A, start, mid-1)
        find_magic_index_nondistinct(A, mid+1, end)
        
find_magic_index_nondistinct.result = []


if __name__=='__main__':
    A=[-40,-20,-1,1,2,3,5,7,9,12,13]
    find_magic_index_distinct(A, 0, len(A)-1)
    print find_magic_index_distinct.result
    find_magic_index_distinct.result=[]
    B=[0,1,2,3]
    find_magic_index_distinct(B, 0, len(B)-1)
    print find_magic_index_distinct.result
    
    
    C=[-10,-5,2,2,2,3,4,7,9,12,13]
    find_magic_index_nondistinct(C, 0, len(C)-1)
    print find_magic_index_nondistinct.result
    