''' Given n non-negative integers representing an elevation map where the width of each bar is 1, 
    compute how much water it is able to trap after raining.
    E.g
        Input: [0,1,0,2,1,0,1,3,2,1,2,1]
        Output: 6
    |                      ___
    |          ___        |  |___   ___
    |   __    |  |__    __|     |__|  |___
    |__|__|___|____|___|_________________|__
'''

''' Idea: for each bar, find the max height bar on the left and right. 
    then for this bar it can hold min(max_left, max_right) - height
    scan from left and then scan from right
'''

def trapping_rain_water(A):
    left_max=[None]*len(A)
    maximum = 0
    volumn=0
    # i = 0...len(A)-1
    for i in range(len(A)):
        left_max[i] = maximum
        maximum = max(maximum, A[i])
    maximum = 0
    # i = len(A)-1 ... 0
    for i in range(len(A)-1, -1, -1):
        bottleneck = min(left_max[i], maximum)
        if bottleneck > A[i]:
            volumn += bottleneck-A[i] 
        maximum = max(maximum, A[i])

    return volumn
    
if __name__=='__main__':
    test_cases=[[2,1,0,1,2],[0,1,0,2,1,0,1,3,2,1,2,1], [4,2,3]]
    for each_test_case in test_cases:
        print each_test_case, trapping_rain_water(each_test_case)
            