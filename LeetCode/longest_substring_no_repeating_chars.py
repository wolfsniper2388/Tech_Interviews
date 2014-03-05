''' Given a string, find the length of the longest substring without repeating characters. 
    E.g 
        Input: 'abcabcbb'
        Output: 'abc'
        Input: 'bbbbb'
        Output: 'b'
'''

def find_longest_substring_no_repeating_chars(s):
    max_len = 0
    exist = [0 for i in range(256)]
    ''' i: index of previously occurred char, j : index of current char
        e.g. s = 'abcdcef'
             when j = 4, i = 2
    ''' 
    i=j=0       
    while j < len(s):
        if exist[ord(s[j])]:
            # update max_len
            max_len = max(max_len, j-i)
            # find i and delete all chars in table before i
            while s[i]!=s[j]:
                exist[ord(s[i])] = 0
                i+=1
            i+=1
            j+=1
        else:
            exist[ord(s[j])] = 1
            j+=1
    return max(max_len, len(s)-i)
        
        
    
if __name__=='__main__':
    test_strings=['yxcdacefh','bbbbbb', 'abcdcef', 'abcdcefgd']
    for each_test_string in test_strings:
        print each_test_string, find_longest_substring_no_repeating_chars(each_test_string)
    
                
            