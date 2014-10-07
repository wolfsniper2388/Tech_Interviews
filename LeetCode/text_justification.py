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
def fullJustify(words, L):
    i=0
    result = []
    while i<=len(words):
        remain = L
        curr_level_str_list = []
        i = one_line_justify(words, L, i, curr_level_str_list)
        
''' justify one line of words starting from index i in words
    return the index in words indicating the end of current level
    str_list is filled after the call
'''     
def one_line_justify(words, L, i, str_list):
    remain = L
    while remain > 0:
        remain -= len(words[i])
        #if remain <0 , pop up the space in the previous iteration
        if remain < 0:
            str_list.pop()
            break
        str_list.extend(words[i])
        remain -= 1
        if remain > 0:
            str_list.append(' ')
        i+=1
    return i
        
if __name__=='__main__':
    test_cases=["This is an example of text justifications", "This is an apple", "This is an erro"]
    for each_test_case in test_cases:
        words = each_test_case.split()
        str_list = []
        print words
        print one_line_justify(words, 16,0, str_list)
        print str_list