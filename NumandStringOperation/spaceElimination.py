''' Remove redundant whitespace in a string, including leading, trailing and those between words of length more than one
    e.g. "   i    like flying  free    " => "i like flying free"
'''

def del_extra_whitespace(str1):
    ch_list=list(str1)
    j=0        # the new string end index
    j_moving=False     # j can move only if: ch_list[i] is not ' ' or it's the first time that ch_list[j] hits ' '
    
    # i always keeps going
    for i in range(len(ch_list)):
        if ch_list[i] !=' ' :
            ch_list[j]=ch_list[i]
            j+=1
            j_moving= True
        elif j_moving:
            ch_list[j]=ch_list[i]
            j+=1
            j_moving = False
    if ch_list[j-1]==' ':
        return ''.join(ch_list)[:j-1]
    else:
        return ''.join(ch_list)[:j]
    
if __name__=='__main__':
    test_cases = ['   i    like flying  free    ', '   i    like flying  free', '   i    like flying  free', 
                  'i    like flying  free  ']
    for each_test_case in test_cases:
        print del_extra_whitespace(each_test_case)
    