'''Given a collection of integers that might contain duplicates, S, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If S = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''
from copy import deepcopy

def subsets(S):
    results = [[]]
    curr_result = []
    S=sorted(S)
    dfs(S, results, curr_result, 0)
    return results
    
def dfs(S,results,curr_result,curr_idx):
    i = curr_idx
    while i < len(S):
        curr_result.append(S[i])
        results.append(deepcopy(curr_result))
        dfs(S,results, curr_result, i+1)
        curr_result.pop()
        while (i < len(S)-1 and S[i] == S[i+1]):
           i+=1
        i+=1
           

if __name__=='__main__':
    test_cases = [[1,2,3], [1,2,2],[5,1,3,6,5], [1,2,3,4,5,6,7,8,10,0]]
    for each_test_case in test_cases:
        print each_test_case, subsets(each_test_case)