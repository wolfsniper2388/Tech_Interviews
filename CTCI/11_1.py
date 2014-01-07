''' Given two sorted arrays A and B, len(A) > len(B) assume A has enough space to hold B.
    write a method to merge B into A in sorted order
'''


''' start from last and move backward
'''
def merge_arrays(A,B):
    last_A=len(A)-1     # last index of A
    last_B=len(B)-1     # last index of B
    merge_index=len(A)+len(B)-1     # last index of A+B
    A=A+[None]*len(B)       # expand A
    while last_A >= 0 and last_B >= 0:
        if B[last_B] > A[last_A]:
            A[merge_index] = B[last_B]
            last_B-=1
        else:
            A[merge_index] = A[last_A]
            last_A-=1
        merge_index-=1
    
    # last_A hits -1, A has been iterated through
    while last_B >= 0:
        A[merge_index] = B[last_B]
        last_B-=1
        merge_index-=1
        
    return A
        
if __name__=='__main__':
    print merge_arrays([1,3,5], [2,4,6])
    print merge_arrays([1,2,3], [4,5,6])
    print merge_arrays([4,5,6], [1,2,3])