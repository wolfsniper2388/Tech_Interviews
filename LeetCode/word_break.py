''' Q1.
    Given a string s and a dictionary of words dict, 
    determine if s can be segmented into a space-separated sequence of one or more dictionary words.
    E.g.
        Input: s = 'leetcode'
               dict = ['leet', 'code']
        Output True
    
    Q2.
    Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.
    Return all such possible sentences.
    E.g.
        Input: s = 'catsanddog'
               dict = ['cat' 'cats', 'and', 'sand', 'dog'].
        Output: ['cats and dog', 'cat sand dog'].
'''


''' Dynamic Programming
    Define can_break[i] = True if s[:i] can be broken into words in d
                          False otherwise
    Suppose I know can_break[0..i-1], then
    can_break[i] = True if for j = i-1 to 0, can_break[j] is True and s[j:i] is in d
                   False otherwise
    take s= 'california'
         d = ['ca','nia', 'for', 'li'] as an example
    when i=4 (s[i] = 'f')
    j = 3, 'i' is not in d
    j = 2, 'li' is in d and can_break[2] is True
    so can_break[4] = True
    can_break is of length len(s)+1
    we return the value can_break[len(s)]. can_break[len(s)] is the value that if s[0:len(s)-1] can be broken into words in d
    that is exactly what we want to return
    Time complexity: O(n*setL*wordL)
'''
def word_break_q1(s,d):
    can_break = [False for i in range(len(s)+1)]
    can_break[0]=True
    for i in range(1, len(s)+1):
        # j = i-1, i-2 ... 0
        for j in range(i-1, -1, -1):
            if can_break[j] and s[j:i] in d:
                can_break[i] = True
                break
    return can_break[len(s)]


from copy import deepcopy

def dfs(s, start, curr_result, results, d):
    # recursion exit
    if start >= len(s):
        results.append(deepcopy(curr_result))
        return
    
    # for i = start to n/n+1
    for i in range(start+1, len(s)+1):
        if s[start:i] in d:
            # extend
            curr_result.append(s[start:i])
            # recursion
            dfs(s, i, curr_result, results, d)
            # pruning
            curr_result.pop()
            
            
def word_break_q2(s,d):
    results = []
    if not word_break_q1(s,d):
        return results
    curr_result = []
    dfs(s, 0, curr_result, results, d)
    string_results=[]
    for each_result in results:
        string_results.append(' '.join(each_result))
    return string_results
    

if __name__=='__main__':
    print 'Q1'
    test_cases = [('california',['ca','for','ni','a','la']), ('aaaaaaa',['aaaa','aaa','aa','a']), ('leetcode',['leet','code'])]
    for each_test_case in test_cases:
        s,d = each_test_case
        print s,d,word_break_q1(s,d)
    print 'Q2'
    test_cases = [('catsanddog',['cat','cats','and','sand','dog']),('aaaa',['a','aa'])]
    for each_test_case in test_cases:
        s,d=each_test_case
        print s,d,word_break_q2(s,d)