''' Given an integer n, return the number of trailing zeroes in n!.

    Note: Your solution should be in logarithmic time complexity.
'''

def trailing_zeros(n):
    count = 0 
    x = 5
    while n / x > 0:
        count += n/x
        x *= 5
    return count

if __name__=='__main__':
    test_cases = [2,5,6,25,26,124,125,127]
    for each_test_case in test_cases:
        print each_test_case, trailing_zeros(each_test_case)