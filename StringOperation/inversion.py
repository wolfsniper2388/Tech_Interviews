''' Invert the chars/words in a string
    
    Example:
        input: 'hello world'
        output: 'dlrow olleh'
        output: 'world hello'
'''

# invert every char in a string
def invert_char(str):
    str_list=list(str)
    start=0
    end=len(str_list)-1
    while start <= end:
        str_list[start],str_list[end]=str_list[end],str_list[start]     # swap
        start+=1
        end-=1
    return ''.join(str_list)
        
        
#invert every word in a string
def invert_word(str):
    result_str=[]
    inverted_str=invert_char(str)       # 'dlrow olleh'
    for each_split in inverted_str.split():     # ['dlrow', 'olleh']
        result_str.append(invert_char(each_split))  #['world', 'hello']
    return ' '.join(result_str)

    
if __name__=='__main__':
    str='hello world!'
    print invert_char(str)
    print invert_word(str)