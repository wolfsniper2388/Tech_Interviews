''' Implement a string compression algorithm:
    Requirement:    
        Use number to represent the repetition times of the continuous chars
        If the length of compressed string is longer than the original one, return the original one
    Example:
        Input: aaabbcccc
        Output: a3b2c4
        Inout: abc
        Output: abc
    
'''

def string_compression(orig_str):
    orig_str_list = list(orig_str)
    result_str_list=[]
    prev_ch=orig_str_list[0]
    count=1
    # the iteration starts from index 1 not 0
    for curr_ch in orig_str_list[1:]:
        # Always compare the current char with the previous char
        if curr_ch == prev_ch:
            count+=1
        else:
            result_str_list.append(prev_ch)
            result_str_list.append(str(count))
            count=1
            prev_ch = curr_ch
    
    # append the last ch
    result_str_list.append(prev_ch)
    result_str_list.append(str(count))
    
    if len(result_str_list) < len(orig_str_list):
        return ''.join(result_str_list)
    else:
        return orig_str
    
if __name__=='__main__':
    print string_compression('aaabbccccd')
    print string_compression('abc')