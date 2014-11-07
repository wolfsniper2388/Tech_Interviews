''' compute sqrt(x, precision), assume x is double, the result will be rounded to precision
'''

from __future__ import division
import math

''' get the square root of x with precision p
'''
def sqrt(x, p):
    if x<0 or p<0:
        return -1
    x_copy = x
    x = x if x>1 else x*100
    start = 0.0
    end = x
    
    while 1:
        m = round((start+end)/2,p)
        if x < m*m:
            end = m
        elif m*m <= x < (m+10**-p)*(m+10**-p) :
            return m if x_copy>1 else round(m/10, p)
        else:
            start = m

if __name__ == '__main__':
    test_cases = [(10,2), (25,4), (11.2, 3),(-5,3), (0,2), (1,2), (2,3), (0.82,2), (37,0)]
    for each_test_case in test_cases:
        x,p = each_test_case
        print x,p,sqrt(x,p)