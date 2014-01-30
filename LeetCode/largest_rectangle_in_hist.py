''' Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, 
    find the area of largest rectangle in the histogram.
    E.g
        Input: [6,1,5,4,4,5,1,6]
        Output: 16 (4*4=16)
        Input: [1,1,3,1,1,1]
        Output: 6 (1:6 = 6)
'''

def larget_rectangle_in_hist(A):
    i = 0
    max_area = 0
    stack = []
    while i < len(A):
        if not stack or A[i]>=A[stack[-1]]:
            stack.append(i)
            i+=1
        else:
            tmp = stack.pop()
            if not stack:
                max_area = max(max_area, A[tmp]*i)
            else:
                max_area = max(max_area, A[tmp] * (i-stack[-1]-1))
    while stack:
        tmp = stack.pop()
        if not stack:
            max_area = max(max_area, A[tmp]*i)
        else:
            max_area = max(max_area, A[tmp] * (i-stack[-1]-1))
    return max_area
            
if __name__=='__main__':
    test_cases = [[6,1,5,4,4,5,1,6], [1,1,3,1,1,1]]
    for each_test_case in test_cases:
        print each_test_case, larget_rectangle_in_hist(each_test_case)