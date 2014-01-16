''' There are two sorted arrays A and B of size m and n respectively. 
    Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
    median is defined to be the middle one if sorted array length is odd
                            the mean of the middle two numbers if sorted array length is even
'''

def median_search(A, B, left, right):
    # the actual median in B
    if left > right:
        total_length = len(A)+len(B)
        initial_left = max(1, total_length/2 - len(A))
        initial_right = min (len(B), total_length/2)
        return median_search(B, A, initial_left, initial_right)
    total_length = len(A)+len(B)
    # suppose A[i] is median
    i = (left+right)/2
    # if A[i] is median, it should be larger than exactly n/2-i number of elements in B 
    j = total_length/2-i-1
    # A[i] is not median, the actual median is at left or in B
    if j < len(B)-1 and A[i] > B[j+1]:
        return median_search(A, B, left, i-1)
    # A[i] is not median, the actual median is at right or in B
    elif j>0 and A[i] < B[j]:
        return median_search(A, B, i+1, right)
    # B[j] < A[i] < B[j+1], then A[i] is the median
    else:
        # if total length is odd, return A[i] directly
        if total_length % 2 == 1:
            return A[i]
        # if total length is even, and i>0, return the mean number
        elif i>0:
            return (A[i]+max(A[i-1], B[j]))/2
        else:
            return (A[i]+B[j])/2
    
if __name__=='__main__':
    A=[1,5,8,12,15,18,21]
    B=[2,7,14]
    total_length=len(A)+len(B)
    initial_left = max(1, total_length/2 - len(B))
    initial_right = min (len(A), total_length/2)
    print median_search(A, B, initial_left, initial_right)