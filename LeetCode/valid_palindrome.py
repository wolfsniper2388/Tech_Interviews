''' Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
'''

def is_letter(ch):
    return 'a'<=ch<='z' or 'A'<=ch<='Z' or '0'<=ch<='9'

def is_same(ch1, ch2):
    return (ch1 == ch2) or (ord(ch1)-ord('A') == ord(ch2)-ord('a')) or (ord(ch1)-ord('a') == ord(ch2)-ord('A'))
    
def is_palindrome(s):
    if not s:
        return True
    i = 0
    j = len(s)-1
    while i < j:
        if not is_letter(s[i]):
            i+=1
            continue
        if not is_letter(s[j]):
            j-=1
            continue
        if not is_same(s[i],s[j]):
            return False
        i+=1
        j-=1
    return True


if __name__=='__main__':
    test_cases = ['A man, a plan, a canal: Panama', 'race a car']
    for each_test_case in test_cases:
        print each_test_case, is_palindrome(each_test_case)