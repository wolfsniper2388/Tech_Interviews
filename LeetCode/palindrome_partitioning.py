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

def is_palindrome_q1(string, start, end):
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
        if is_palindrome_q1 (s, start, end):
            curr_result.append(s[start:end+1])
            palindrome_partition_q1_helper(s,end+1, curr_result, results)
            curr_result.pop()
    return results


def is_palindrome_q2(string, string_hash):
    if string in string_hash:
        #print string,'is in string hash'
        return string_hash[string]
    start = 0
    end = len(string)-1
    while start < end:
        if string[start] != string[end]:
            string_hash[string] = False
            return False
        start += 1
        end -= 1
    string_hash[string] = True
    return True

''' Let s = 'abcddcb'
    Suppose I know all the minimal cuts from i+1 to n-1 (end), how can I infer the minimal cuts at index i? 
    let min_cuts[i] be the number of minimum cuts from i to n-1, as said, suppose I know min_cuts[i+1], min_cuts[i+2], ... min_cuts[n-1]
    then min_cuts[i] = min(min_cuts[i], min_cuts[j+1]+1) for j = i to n-1
    we should only update min_cuts[i] if s[i:j+1] (s[i],s[i+1] ... s[j] ) is a palindrome
    How can we do that? scan the substring each time? actually we can have a hash map to store if a substring is a palindrome or not
    and this can be encapsulated in a function call: palindrome_partition_q2
    What's the initial min_cuts[i] for i = 0 to n-1 ?  we will assume the worst possible case where no substring is palindrome, so 
    the initial value of min_cuts[i] = len(s) - i -1
    take s =                   'a b c d d c b' as an example
    the final min_cuts will be [1,0,1,2,2,1,0,-1]
'''
def palindrome_partition_q2(s):
    min_cuts = [len(s)-i-1 for i in range(len(s)+1)]
    string_hash = {}
    for i in range(len(s)-1, -1,-1):
        for j in range(i, len(s)):
            if is_palindrome_q2(s[i:j+1], string_hash):
                min_cuts[i] = min(min_cuts[i], min_cuts[j+1]+1)
    return min_cuts[0]


if __name__=='__main__':
    test_cases = ['aaa', 'bcddeffeh', 'aab', 'ababbbabbaba', 'abcddcb', 'a', 'bcdeffhh']
    for each_test_case in test_cases[-1:]:
        print 'Q1'
        print each_test_case, palindrome_partition_q1(each_test_case)
        print 'Q2'
        print each_test_case, palindrome_partition_q2(each_test_case) 