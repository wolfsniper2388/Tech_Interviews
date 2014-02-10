''' Q1.
    Given a string s, partition s such that every substring of the partition is a palindrome.
    Return all possible palindrome partitioning of s.
    E.g
        Input: 'bcddeffeh'
        Output: ['dd','ff','effe','b','c','d','e','f','h']
        
    Q2.
    Given a string s, partition s such that every substring of the partition is a palindrome.
    Return the minimum cuts needed for a palindrome partitioning of s.
    E.g.
        Input: 'aab'
        Output: 1, (aa|b)
'''


'''
The classic recursion structure to enumerate all the possible set cuts
def foo(results, one_result, array, start): 
    if start < s.size():
        size_t pos = start
    while pos < s.size():
        one_result.append
        foo(result, one_result, s, pos + 1);
        one_result.pop
        pos+=1
    else:
        got one solution
    
'''

from copy import deepcopy
def is_palindrome(string, start, end):
    while start < end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1
    return True


def palindrome_partition_q1(s):
    return palindrome_partition_q1_helper(s, 0, [],[])
    
def palindrome_partition_q1_helper(s,start, curr_result, results):
    if start >= len(s):
        results.append(deepcopy(curr_result))
        return results
    for end in range(start, len(s)):
        if is_palindrome (s, start, end):
            curr_result.append(s[start:end+1])
            palindrome_partition_q1_helper(s,start+1, curr_result, results)
            curr_result.pop()
    return results
     
if __name__=='__main__':
    test_cases = ['aaa', 'bcddeffeh', 'aab']
    for each_test_case in test_cases:
        print each_test_case, palindrome_partition_q1(each_test_case)