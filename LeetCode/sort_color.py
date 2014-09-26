''' Given an array with n objects colored red, white or blue, 
    sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.
    Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
    Note: You are not suppose to use the library's sort function for this problem.
    A rather straight forward solution is a two-pass algorithm using counting sort.
    First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, 
    then 1's and followed by 2's.
    Could you come up with an one-pass algorithm using only constant space?
    E.g.
    Input: [1,0,2,1,2,0,1,1]
    Output: [0,0,1,1,1,1,2,2]
'''

''' like quick sort pivot
    i is the boundary of 0 and 1
    j is the boundary of 1 and 2
    iterate through A with index curr
    if A[curr] == 0, swap A[curr] and A[i], i++, curr++
    if A[curr] ==1, swap A[curr] and A[j], j-- (no curr++ here, beacuse A[j] might be 0, need to swap A[curr] and A[i] then)
    else curr++
'''
def sort_color(A):
    # i means all the elements before index i (exclusive) should be 0
    i = 0
    # j means all the elements after index j(exclusive) should be 2
    j = len(A)-1
    curr = i
    while curr <= j:
        if A[curr] == 0:
            A[curr],A[i]=A[i],A[curr]
            i+=1
            curr+=1
        elif A[curr] == 2:
            A[curr],A[j]=A[j],A[curr]
            # curr can not increase here because A[j] might be 0
            j-=1
        else:
            curr+=1
    return A

if __name__=='__main__':
    test_cases = [[1,0,2,1,2,0,1,0], [0,0,1,2,2,1,0]]
    for each_test_case in test_cases:
        print each_test_case, sort_color(each_test_case)