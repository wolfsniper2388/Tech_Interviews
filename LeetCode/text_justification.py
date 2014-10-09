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

''' insert extra spaces to the current level from @param start in words to @param end-1 in words
'''
def insert_extra_spaces(str_list, start, end, L, words):
    n_extra_spaces = L-len(str_list)
    n_words = end-start
    #if only one word in the current line or it's the last line, simply append the extra spaces 
    if (n_words == 1 or end == len(words)):
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
def one_line_termintation(words, L, i, str_list):
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
    i=0     #current level start index in words
    j=0     #next level start index in words
    result = []
    #invalid input
    if L==0:
        return [""]
    #invalid input
    for word in words:
        if L<len(word):
            return [""]
    while i<len(words):
        remain = L
        curr_level_str_list = []
        # first decide where do we stop for the current level
        j = one_line_termintation(words, L, i, curr_level_str_list)
        # next insert the extra spaces
        insert_extra_spaces(curr_level_str_list,i,j,L,words)
        result.append(''.join(curr_level_str_list))
        i=j
    return result
        
if __name__=='__main__':
    test_cases=[("This is an example of text justifications",16), ("This is an apple",16), ("This is an erro",16), ("This is ant",16), 
                ("hello this is my first programming test in python",16), ("a b c d e",1), ("",0), ("what must be shall be.",12)]
    for each_test_case in test_cases:
        words,L = each_test_case
        words=words.split()
        str_list = []
        print words
        print full_justify(words, L)