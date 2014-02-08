''' Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
    E.g
        Input: ' A man3, a plan, a canal: Pa3nama    '
        Output: True
        Input: 'race a car'
        Output: False
'''

def is_alphanumeric(ch):
    return 'a'<=ch<='z' or 'A'<=ch<='Z' or '0'<=ch<='9'

def is_uppercase(ch):
    return 'A'<=ch<='Z'


def is_valid_palindrome_str(orig_str):
    s = list(orig_str)
    if not s:
        return True
    i = 0
    j = len(s)-1
    while i < j:
        # skip all non alphanumeric chars
        while i<len(s) and not is_alphanumeric(s[i]):
            i+=1
        while j>=0 and not is_alphanumeric(s[j]):
            j-=1
        
        if i == len(s) and j == -1:
            return True
        # if uppercase, lower it
        if is_uppercase(s[i]):
            s[i] = s[i].lower()
        if is_uppercase(s[j]):
            s[j] = s[j].lower()
        # palindrome check
        if s[i] == s[j]:
            i+=1
            j-=1
        else:
            return False
    return True


if __name__=='__main__':
    test_cases = [' A man, a plan, a canal: Panama    ', 'race a car', '', 'abb   a', '.,', 'a.', '1a2']
    for each_test_case in test_cases:
        print each_test_case, is_valid_palindrome_str(each_test_case)