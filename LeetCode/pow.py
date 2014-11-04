''' Implement pow(x, n)
'''
from __future__ import division

def pow(x,n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return pow(x, int(n/2)) * pow(x, int(n/2))
    elif n>0:
        return pow(x, int(n/2)) * pow(x, int(n/2)) *x
    else:
        return pow(x, int(n/2)) * pow(x, int(n/2)) / x


if __name__ == '__main__':
    test_cases = [(2,3), (2, -5), (3, 7) , (2,4)]
    for each_test_case in test_cases:
        x,n = each_test_case
        print x,n,pow(x,n)