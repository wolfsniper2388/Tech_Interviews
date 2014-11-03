''' Given a triangle, find the minimum path sum from top to bottom. 
    Each step you may move to adjacent numbers on the row below.
    E.g
        Input:
                [
                     [2],
                    [5,4],
                   [6,5,7],
                  [4,1,8,3]
                ]
         Output: 12 (2+4+5+1)        
 
'''

import sys
from copy import *

def min_path_1(T):
    min_sum, min_sum_path = dfs(T,0,0,0,[],[sys.maxint],[])
    return min_sum, min_sum_path
    
# top_down
def dfs(T,i,j,curr_sum,curr_sum_path, min_sum, min_sum_path):
    curr_sum += T[i][j]
    curr_sum_path.append(T[i][j])
    if i == len(T)-1:
        if curr_sum < min_sum[0]:
            min_sum[0] = curr_sum
            # min_sum_path = deepcopy(curr_sum_path) will not work here, because min_sum_path is now a name tagged to a new object which is invisible outside recursion
            # so clear min_sum_path first(using del min_sum_path [:] or using min_sum_path[:] = []) and then extend curr_sum_path
            del min_sum_path [:] 
            min_sum_path.extend(curr_sum_path)
        return (min_sum[0], min_sum_path)
    next_i = i+1
    # next_j = j, j+1
    for next_j in range(j,j+2):
        dfs(T,next_i,next_j,curr_sum,curr_sum_path, min_sum, min_sum_path)
        curr_sum_path.pop()
    return (min_sum[0], min_sum_path)

# bottom-up
def min_path_2(T):
    n = len(T)-1
    p=[0]*(n+2)
    while n >= 0:
        for i in range(n+1):
            p[i] = T[n][i]+min(p[i],p[i+1])
        n-=1
    return p[0]
    

if __name__=='__main__':
    test_case=[[2],[5,4],[6,5,7],[4,1,8,3]]
    min_sum, min_sum_path = min_path_1(test_case)
    print test_case, min_sum, min_sum_path
    print test_case, min_path_2(test_case)