''' implement atoi function which converts a string to a integer
    Requirements for atoi:
        The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. 
        Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible,
        and interprets them as a numerical value.

        The string can contain additional characters after those that form the integral number, 
        which are ignored and have no effect on the behavior of this function.

        If the first sequence of non-whitespace characters in str is not a valid integral number, 
        or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

        If no valid conversion could be performed, a zero value is returned. 
        If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
        
    E.g
        Input: '123'
        Output: 123
        Input: '     -0456@fthfa'
        Output: -456
'''

import sys

def atoi(orig_str):
    if orig_str == '':
        return 0
    
    ch_list=list(orig_str)
    num=0
    sign=1
    i=0
    while ch_list[i] == ' ':
        i+=1
    
    if ch_list[i] == '-':
        sign=-1
        i+=1
    if ch_list[i] == '+':
        sign=1
        i+=1
    while i<len(ch_list) and '0'<=ch_list[i]<='9':
        if num > 214748364 or (num == 214748364 and int(ch_list[i])-int('0')>7):
            return sys.maxint*sign
        num = num*10+int(ch_list[i])-int('0')
        i+=1
    return num*sign

if __name__=='__main__':
    test_cases=['   123', '@58fui', '    -214748364785@f45%']
    for each_test_case in test_cases:
        print each_test_case, atoi(each_test_case)
    
    
    
    
     
        