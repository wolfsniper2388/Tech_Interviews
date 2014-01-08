''' Invert the chars/words in a string
    
    Example:
        input: 'hello world'
        output: 'dlrow olleh'
        output: 'world hello'
'''

''' invert every char in a string
    @param string: the string to be char-inverted
    @return: char-inverted string in string type 
'''
def invert_char(string):
    ch_list=list(string)
    start=0
    end=len(ch_list)-1
    while start <= end:
        ch_list[start],ch_list[end]=ch_list[end],ch_list[start]     # swap
        start+=1
        end-=1
    return ''.join(ch_list)
        
        
''' invert every word in a string
    @param string: the string to be word-inverted
    @return: word-inverted string of string type 
'''
def invert_word(string):
    result_ch_list=[]
    inverted_str=invert_char(str)       # '!dlrow olleh'
    for each_split in inverted_str.split():     # ['dlrow', 'olleh']
        result_ch_list.append(invert_char(each_split))  #['world', 'hello']
    return ' '.join(result_ch_list)

    
if __name__=='__main__':
    str='hello world!'
    print invert_char(str)
    print invert_word(str)