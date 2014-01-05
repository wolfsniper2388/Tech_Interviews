''' Remove redundant whitespace in a string, including leading, trailing and those between words of length more than one
    e.g. "   i    like flying  free    " => "i like flying free"
'''

def del_extra_whitespace(str1):
    str_list=list(str1)
    j=0        # the new string end index
    j_moving=False     # j can move only if: str_list[i] is not ' ' or it's the first time that str_list[j] hits ' '
    
    # i always keeps going
    for i in range(len(str_list)):
        if str_list[i] !=' ' :
            str_list[j]=str_list[i]
            j+=1
            j_moving= True
        elif j_moving:
            str_list[j]=str_list[i]
            j+=1
            j_moving = False
    if str_list[j-1]==' ':
        return ''.join(str_list)[:j-1]
    else:
        return ''.join(str_list)[:j]
    
if __name__=='__main__':
    print del_extra_whitespace('   i    like flying  free    ')
    print del_extra_whitespace('   i    like flying  free')
    print del_extra_whitespace('i    like flying  free  ')
    print del_extra_whitespace('i    like flying  fs')