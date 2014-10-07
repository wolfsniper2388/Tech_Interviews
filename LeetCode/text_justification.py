'''Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.
Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
'''

def insert_extra_spaces(str_list, start, end, L, words):
    n_extra_spaces = L-len(str_list)
    n_words = end-start
    if (n_words == 1):
        str_list.extend([' ']*n_extra_spaces)
        return
    average_space = n_extra_spaces / (n_words-1)
    mod_remain = n_extra_spaces % (n_words-1)
    insert_pos = len(words[start])
    for i in range(start,end-1):
        if mod_remain>0:
            str_list[insert_pos:insert_pos] = [' ']*(average_space+1)
            mod_remain -= 1
            insert_pos += average_space+1+1+len(words[i+1])
        else:
            str_list[insert_pos:insert_pos] = [' ']*(average_space)
            insert_pos += average_space+1+len(words[i+1])

''' justify one line of words starting from index i in words
    return the index in words indicating the end of current level
    str_list is filled after the call
'''     
def one_line_justify(words, L, i, str_list):
    remain = L
    while i<len(words) and remain > 0:
        remain -= len(words[i])
        #if remain <0 , pop up the space in the previous iteration
        if remain < 0:
            str_list.pop()
            break
        str_list.extend(words[i])
        i+=1
        remain -= 1
        if remain > 0 and i<len(words):
            str_list.append(' ')
        
    return i


def full_justify(words, L):
    i=0
    j=0
    result = []
    if L==0:
        return []
    while i<len(words):
        remain = L
        curr_level_str_list = []
        j = one_line_justify(words, L, i, curr_level_str_list)
        insert_extra_spaces(curr_level_str_list,i,j,L,words)
        result.append(''.join(curr_level_str_list))
        i=j
    return result
        
        

        
if __name__=='__main__':
    test_cases=["This is an example of text justifications", "This is an apple", "This is an erro", "This is ant", "hello this is my first programming test in python", ""]
    for each_test_case in test_cases:
        words = each_test_case.split()
        str_list = []
        print words
        '''
        j = one_line_justify(words, 16,0, str_list)
        print j
        print str_list
        insert_extra_spaces(str_list, 0, j , 16, words) 
        print str_list
        '''
        print full_justify(words, 16 )