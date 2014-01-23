''' Given n non-negative integers representing an elevation map where the width of each bar is 1, 
    compute how much water it is able to trap after raining.
    E.g
        Input: [0,1,0,2,1,0,1,3,2,1,2,1]
        Output: 6
    |                      __
    |          ___        |  |___   ___
    |   __    |  |__    __|     |__|  |___
    |__|__|___|____|___|_________________|__
'''

''' Idea: find the first number A[j] >= the current one A[i]
    sum += sigma (A[i] - A[k]), for i<k<j
'''

def trapping_rain_water(A):
    i = 0
    j = 0
    sum = 0
    temp_sum = 0
    while j < len(A):
        if A[j] < A[i]:
            temp_sum += A[i]-A[j]
        else:
            sum+=temp_sum
            temp_sum = 0
            i=j
        j+=1
    return sum


if __name__=='__main__':
    test_cases=[[2,1,0,1,2],[0,1,0,2,1,0,1,3,2,1,2,1]]
    for each_test_case in test_cases:
        print each_test_case, trapping_rain_water(each_test_case)
            