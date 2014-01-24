''' Given an array of non-negative integers, you are initially positioned at the first index of the array.
    Each element in the array represents your maximum jump length at that position.
    Determine if you are able to reach the last index.
    E.g
        Input: [2,3,1,1,4]
        Output: True
        Input: [3,2,1,0,4]
'''
''' record the 0's position
    0s are pits
    for each A[i]=0
    check if there exists A[j] > i-j where j < i
'''

def jump_game(A):
    
                