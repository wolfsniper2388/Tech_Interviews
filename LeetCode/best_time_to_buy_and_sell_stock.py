''' Q1.
    Given an array A, maximize: A[i]-A[j], where i>j
'''

def buy_sell_stock_q1(A):
    min = max_diff = start = end = 0
    for i in range(len(A)):
        if A[i] < A[min]:
            min = i
        diff = A[i] - A[min]
        if diff > max_diff:
            max_diff = diff
            start = min
            end = i
    return (A[start],A[end])

if __name__=='__main__':
    test_cases = [[5,4,3,2,9,6,0,8],[3,1,5,6,2,9,-1,2,9,8]]
    for each_test_case in test_cases:
        A = each_test_case
        print A, buy_sell_stock_q1(A) 