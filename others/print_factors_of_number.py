'''Write a program that takes an integer and prints out all ways to multiply smaller integers that equal the original number, without repeating sets of factors. In other words, if your output contains 4 * 3, you should not print out 3 * 4 again as that would be a repeating set. Note that this is not asking for prime factorization only. Also, you can assume that the input integers are reasonable in size; correctness is more important than efficiency.

PrintFactors(12)

12 * 1
6 * 2
4 * 3
3 * 2 * 2

PrintFactors(32)

32 * 1
16 * 2
8 * 4
8 * 2 * 2
4 * 4 * 2
4 * 2 * 2 * 2
2 * 2 * 2 * 2 * 2

PrintFactors (96)
96 * 1
48 * 2
32 * 3
24 * 4
24 * 2 * 2
16 * 6
16 * 3 * 2
12 * 8
12 * 4 * 2
12 * 2 * 2 * 2
8 * 6 * 2
8 * 4 * 3
8 * 3 * 2 * 2
6 * 4 * 4
6 * 4 * 2 * 2
6 * 2 * 2 * 2 * 2
4 * 4 * 3 * 2
4 * 3 * 2 * 2 * 2
3 * 2 * 2 * 2 * 2 * 2
'''

from copy import deepcopy
from math import *

def find_factors(n):
    results = []
    curr_result = []
    num_map = {}
    '''
    find_factors_helper(n,results, curr_result)
    return results'''
    return find_factors_helper(n, num_map)

'''
def find_factors_helper(n, results, curr_result):
    for i in range(2, int(floor(sqrt(n)))+1):
        if n % i == 0:
            curr_result.append(i)
            curr_result.append(n/i)
            tmp = sorted(curr_result)
            if tmp not in results:
                results.append(deepcopy(tmp))
            curr_result.pop()
            find_factors_helper(n/i, results, curr_result)
            curr_result.pop()
'''
def find_factors_helper(n, num_map):
    if n<=3:
        return [[n]]
    if n in num_map:
        #print 'hits', n, num_map[n]
        return num_map[n]
    num_map[n] = []
    for i in range(2, int(floor(sqrt(n)))+1):
        if n % i == 0:
            prev_results = find_factors_helper(n/i, num_map)
            prev_results_copy = deepcopy(prev_results)
            prev_results_copy.append([n/i])
            for j in range(len(prev_results_copy)):
                prev_results_copy[j].append(i)
                prev_results_copy[j] = sorted(prev_results_copy[j])
                if prev_results_copy[j] not in num_map[n]:
                    num_map[n].append(prev_results_copy[j])
    return num_map[n]

if __name__=='__main__':
    test_cases = [12,24,32,96]
    for each_test_case in test_cases:
        print each_test_case, find_factors(each_test_case)