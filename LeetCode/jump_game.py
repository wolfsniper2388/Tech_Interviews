''' Q1
    Given an array of non-negative integers, you are initially positioned at the first index of the array.
    Each element in the array represents your maximum jump length at that position.
    Determine if you are able to reach the last index.
    E.g
        Input: [2,3,1,1,4]
        Output: True
        Input: [3,2,1,0,4]
        Output: False

    Q2. Given an array of non-negative integers, you are initially positioned at the first index of the array.
    Each element in the array represents your maximum jump length at that position.
    Determine if you are able to reach the last index.
    E.g
        Input: [2,3,1,1,4]
        Output: 2
        Input: [3,2,1,0,4]
        Output: maxint
'''
import sys

def jump_game_q1(A):
    reach = 1
    i = 0
    while i < len(A):
        if i < reach:
            reach  = max(reach, A[i]+i+1)
        i+=1
    return reach >= len(A)


''' Idea: Dynamic Programming
    steps[i] = min (steps[j] ) where A[j]+j >= i and j<i)
'''
def jump_game_q2(A):
    if len(A) == 1:
        return 0
    if A[0]==0:
        return sys.maxint
    steps=[None]*len(A)
    steps[0]=0
    min_steps = sys.maxint
    for i in range(1, len(A)):
        min_steps = sys.maxint
        for j in range(i):
            if A[j]+j >= i:
                min_steps = min(min_steps, steps[j])
        steps[i] = min_steps+1
        
    return steps[-1]

if __name__=='__main__':
    'Q1'
    print 'Q1'
    test_cases = [[0,1,2,3], [5,3,2,1,0,8], [5,3,2,1,0,2,1,0,8], [4,2,1,0,3,1,0,8]]
    for each_test_case in test_cases:
        print each_test_case, jump_game_q1(each_test_case)
    'Q2'
    print 'Q2'
    test_cases = [[2,4,1,1,1,1,8,6], [0,1,2,3,6], [3,2,1,0,5], [7] ]
    for each_test_case in test_cases:
        print each_test_case, jump_game_q2(each_test_case)