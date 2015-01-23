'''
Given two strings s and t, determine if they are both one edit distance apart.

one edit distance means after changing / adding / deleting one character in s, it's the same as t

e.g.
    s = 'ghi'
    t = 'ghij'
    return true
    
    s = 'anet'
    t = 'amet'
    return true
    

'''

def one_edit_distance(s,t):
    if s == t:
        return False
    if abs(len(s)-len(t)) > 1:
        return False
    i = j = 0
    while i < len(s) and j < len(t):
        if s[i] != t[j]:
            if len(s) == len(t):
                return s[i+1:] == t[j+1:]
            elif len(s) > len(t):
                return s[i+1:] == t[j:]
            else:
                return s[i:] == t[j+1:]
        else:
            i += 1
            j += 1
    return True


if __name__=='__main__':
    test_cases = [('ghi', 'ghijk'), ('ghi', 'ghij'), ('anet', 'amet'), ('hello','hallow'), ('abc','dbc'), ('', 'a'), ('',''), ('a', 'ba')]
    for each_test_case in test_cases:
        s,t = each_test_case
        print s, t, one_edit_distance(s, t)
    