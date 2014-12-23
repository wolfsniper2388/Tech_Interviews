''' Implement regular expression matching with support for '.' and '*'.
    '.' Matches any single character.
    '*' Matches zero or more of the preceding element.

    The matching should cover the entire input string (not partial).

    The function prototype should be:
    bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") -> false
isMatch("aa","aa") -> true
isMatch("aaa","aa") -> false
isMatch("aa", "a*") -> true
isMatch("aa", ".*") -> true
isMatch("ab", ".*") -> true
isMatch("aab", "c*a*b") -> true
isMatch("abcbcd", "a.*c.*d") = true
''' 

def regex_match(string, pattern):
    return is_match(string, pattern, 0, 0)

''' If the next character of p is NOT '*', then it must match the current character of s. 
        Continue pattern matching with the next character of both s and p.
    If the next character of p is '*', then we do a brute force exhaustive matching of 
    0, 1, or more repeats of current character of p Until we could not match any more characters.
'''

def is_match(string, pattern, s_index, p_index):
    # if p_index reaches end (len(pattern)), s_index should also go to end
    if p_index == len(pattern):
        return s_index == len(string)
    
    # if p_index reaches last(len(pattern)-1), s_index must reach last and string and pattern must match at last indices
    if p_index == len(pattern)-1:
        return s_index == len(string)-1 and (string[s_index]==pattern[p_index] or pattern[p_index]=='.')
    
    # if next pattern != '*'
    if pattern[p_index+1] != '*':
        # (string[s_index]==pattern[p_index]) or (pattern[p_index]=='.' and string) means string and pattern can match at current
        # s_index and p_index
        return (((s_index < len(string) and (string[s_index]==pattern[p_index] or pattern[p_index]=='.'))) 
            and is_match(string, pattern, s_index+1, p_index+1))
    
    # if next pattern == '*'
    # while string and pattern can match at current s_index and p_index
    while (s_index < len(string)) and ((string[s_index]==pattern[p_index]) or (pattern[p_index]=='.')):
        # if pattern[p_index+2:] can match string then return True
        # e.g. string = 'abc' pattern = 'a*bc'
        if is_match(string, pattern, s_index, p_index+2):
            return True
        # else, we will see if string and pattern can match at s_index+1 and p_index
        s_index+=1
    # until we could not match any more characters
    return is_match(string, pattern, s_index, p_index+2)

if __name__=='__main__':
    test_cases=[('abc', 'abc'), ('abcd', '.*'), ('abcbcd', 'a.*c.*d'), ('abcbcd', 'a*c.*d'), ('a', 'aa'),
                ('aa', 'a'), ('a', ''), ('', 'a'), ('', 'a*'), ('a', '.*..a'), ('aaaaaaaaaaaaab', 'a*a*a*a*a*a*a*a*a*a*c')]
    for each_test_case in test_cases:
        string,pattern=each_test_case
        print each_test_case, regex_match(string, pattern)