'''Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
'''


def max_subarray_product(A):
    min_negative = A[0]    # minimum negative number till now
    max_positive = A[0]    # maximum positive number till now
    max_product = A[0]
    n = len(A)
    for i in range(1,n):
        tmp = max_positive
        max_positive = max(min_negative*A[i], A[i], max_positive*A[i])
        min_negative = min(min_negative*A[i], A[i], tmp*A[i])
        max_product = max(max_product, max_positive)
    return max_product


if __name__ == '__main__':
    test_cases = [[2,3,-2,4], [-2,-3,7,-6], [0,0,0], [0,0,-20,0], [2,3,-1,0,4], [-2], [-1,5], [-4, -3], [-1,-2,-3,0]]
    for each_test_case in test_cases:
        print each_test_case, max_subarray_product(each_test_case)