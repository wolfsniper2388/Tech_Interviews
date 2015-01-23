'''
Given a string, find the length of the longest substring T that contains at most 2 distinct characters.

For example, Given s = "eceba",

T is "ece" which its length is 3.
'''

def longest_substr_with_at_most_two_distinct_chars(s):
    max_len = 0
    longest_substr = []
    char_map = {}
    i = j = 0
    cnt = 0
    n = len(s)
    if n <= 2:
        return n
    while j < n:
        if s[j] not in char_map:
            char_map[s[j]] = 1
            cnt += 1
        
        if cnt > 2:
            if j-i > max_len:
                max_len = j-i
                max_substr = s[i:j]
            i = j-1
            while s[i-1] == s[i]:
                i -= 1
            del char_map[s[i-1]]
            cnt = 2
        j+=1
    if j-i > max_len:
        max_len = j-i
        max_substr = s[i:j]
    return (max_substr, max_len)

if __name__ == '__main__':
    test_cases = ['eceba', 'ececcbabababaab', 'abc', 'aba','bcbbbayytye', 'abbbcccdddeeee']
    for each_test_case in test_cases:
        print each_test_case, longest_substr_with_at_most_two_distinct_chars(each_test_case)
         