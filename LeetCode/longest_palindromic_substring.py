''' Find the longest palindromic substring in a string
    Assume: there exists one unique longest palindromic substring.
    ref: http://leetcode.com/2011/11/longest-palindromic-substring-part-ii.html
         http://www.felix021.com/blog/read.php?2040
'''

def find_longest_palindrome_substring(orig_str):
    new_str=orig_str
    # pre-process, insert # between letters
    for i in range(0,2*len(new_str)+1, 2):
        new_str = new_str[:i]+'#'+new_str[i:]
    
    # Generate P
    S=list(new_str)
    P=[0 for i in range(len(S))]
    right_bound = 0
    center = 0
    
    for i in range(1,len(S)-1):
        j = 2*center - i
        if right_bound > i:
            if right_bound - i > P[j]:
                P[i] = P[j]
            else:
                P[i] = right_bound - i
        else:
            P[i]=0
            
        while i+1+P[i]<len(S) and S[i+1+P[i]] == S[i-1-P[i]]:
            P[i]+=1
    
        if i+P[i] > right_bound:
            center = i
            right_bound = i+P[i]
        
    # find max in P
    max_len = max(P)
    max_index = P.index(max_len)
    

    return ''.join(S[max_index-max_len: max_index+max_len+1]).replace('#','')

        
    
    
    
if __name__=='__main__':
    print find_longest_palindrome_substring('12212321')