''' Given an array of non-negative integers, you are initially positioned at the first index of the array.
    Each element in the array represents your maximum jump length at that position.
    Determine if you are able to reach the last index.
    E.g
        Input: [2,3,1,1,4]
        Output: True
        Input: [3,2,1,0,4]
'''
import sys
''' record the 0's position
    0s are pits
    for each A[i]=0
    check if there exists A[j] > i-j where j < i
'''

#def jump_game(A):
    


''' Idea: Dynamic Programming
    steps[i] = min (steps[j] ) where A[j]+j >= i and j<i)
'''
def jump_game_q2(A):
    if len(A) == 1:
        return 0
    steps=[None]*len(A)
    steps[0]=0
    min_steps = sys.maxint
    if A[0] == 0:
        steps[1] = sys.maxint
    else:
        steps[1] = 1
    for i in range(2, len(A)):
        for j in range(i):
            if A[j]+j >= i and steps[j] < min_steps:
                min_steps = steps[j]
        steps[i] = min_steps+1
        min_steps = sys.maxint
    return steps[-1]

if __name__=='__main__':
    test_cases = [[2,4,1,1,1,1,8,6], [0,1,2,3,6], [3,2,1,0,5], [7] ]
    for each_test_case in test_cases:
        print each_test_case, jump_game_q2(each_test_case)