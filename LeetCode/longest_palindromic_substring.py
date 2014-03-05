''' Find the longest palindromic substring in a string
    Assume: there exists one unique longest palindromic substring.
    ref: http://leetcode.com/2011/11/longest-palindromic-substring-part-ii.html
         http://www.felix021.com/blog/read.php?2040
'''

def find_longest_palindrome_substring(S):
    S=list(S)
    # pre-process S
    S='#'.join(S)
    S = '#'+S+'#'
       
    # Generate P
    P=[0 for i in range(len(S))]
    right_bound = 0
    center = 0
    
    for i in range(1,len(S)-1):
        j = 2*center - i
        if right_bound > i:
            if right_bound - i > P[j]:
                P[i] = P[j]
            else:
                # P[i] >= right_bound-i, here, just assign minimum to P[i], it will expand in the following while loop
                P[i] = right_bound - i
        else:
            P[i]=0
            
        # expand P[i]    
        while i+1+P[i]<len(S) and i-1-P[i]>=0 and S[i+1+P[i]] == S[i-1-P[i]]:
            P[i]+=1
            
        # update right_bound and center if i+P[i] expands across current right_bound
        if i+P[i] > right_bound:
            center = i
            right_bound = i+P[i]
        
    # find max in P
    max_len = max(P)
    max_index = P.index(max_len)
    

    return ''.join(S[max_index-max_len: max_index+max_len+1]).replace('#','')


if __name__=='__main__':
    test_cases = ['12212321','bb']
    for each_test_case in test_cases:
        print each_test_case, find_longest_palindrome_substring(each_test_case)