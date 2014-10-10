''' Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".
Note: 
    A sequence of non-space characters constitutes a word.
    Your reversed string should not contain leading or trailing spaces
    Reduce multiple spaces between two words to a single space in the reversed string.
'''

''' eliminate the leading and trailing spaces as well as the multiple spaces between two words
'''
def eliminate_extra_spaces(str_list):
    i=0     # index of old str_list
    j=0     # index of new str_list
    n = len(str_list)
    j_move = False
    for i in range(n):
        if str_list[i] != ' ':
            str_list[j]=str_list[i]
            j_move = True
            j+=1
        elif j_move:
            str_list[j]=str_list[i]
            j_move = False
            j+=1
    if j == 0 or str_list[j-1] != ' ':
        return str_list[:j]
        
    return str_list[:j-1]
    
def reverse_string(str_list, start,end):
    while start<end:
        str_list[start],str_list[end] = str_list[end],str_list[start]
        start+=1
        end-=1

def reverse_words_in_string(s):
    if not s:
        return ''
    orig_str_list = list(s)
    new_str_list = eliminate_extra_spaces(orig_str_list)
    reverse_string(new_str_list, 0 ,len(new_str_list)-1)
    start = 0
    end = 0
    if not new_str_list:
        return ''
    new_str_list.append(' ')
    n = len(new_str_list)
    for end in range(n):
        if new_str_list[end] == ' ':
            reverse_string(new_str_list, start, end-1)
            start = end+1
    new_str_list.pop()
    return ''.join(new_str_list)


if __name__ == '__main__':
    test_cases = ['   hello world  i can    say    ', '    ', '',' a ','hi',' 123  987 ']
    for each_test_case in test_cases:
        print 'input:', each_test_case
        print 'output:', reverse_words_in_string(each_test_case)