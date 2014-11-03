''' 
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(s, p)

Some examples:
isMatch("aa","a") -> false
isMatch("aa","aa") -> true
isMatch("aaa","aa") -> false
isMatch("aa", "*") -> true
isMatch("aa", "a*") -> true
isMatch("ab", "?*") -> true
isMatch("aab", "c*a*b") -> false
'''

def is_match(s,p):
    i = 0   # index of s
    j = 0   # index of p
    star_idx = -1   # star index in p 
    match_idx = 0   # matching star index in s
    while i < len(s):
        if j < len(p) and (s[i] == p[j] or p[j] == '?'):
            i+=1
            j+=1
        elif j < len(p) and p[j] == '*':
            match_idx = i
            star_idx = j
            j+=1
        # if there is a previous '*'
        elif (star_idx != -1):
            j = star_idx+1
            match_idx += 1
            i = match_idx
        else:
            return False
    while j < len(p) and p[j] == '*':
        j+=1
    return True if j == len(p) else False


if __name__=='__main__':
    test_cases = [('aa','*'),('abed','?b*d**'), ('aaa','aaa'), ('aaa','aa'), ('aa','a*'), ('ab','?*'), ('bdf', '*?')]
    for each_test_case in test_cases:
        s,p = each_test_case
        print s,p,is_match(s,p)      