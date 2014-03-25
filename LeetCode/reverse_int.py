''' Reverse every digit in an integer
    E.g
        Input: 123
        Output: 321
        Input: -123
        Output: -321
'''

def reverse_int(orig_int):
    sign=1
    if orig_int<0:
        sign=-1
    
    orig_int = abs(orig_int) 
    
    orig_div=1
    orig_int_copy=orig_int
    while orig_int_copy >= 10:
        orig_div *= 10
        orig_int_copy /= 10
    
    new_int=0
    new_div=1
    
    while orig_div > 0:
        curr_digit = orig_int / orig_div
        new_int+=curr_digit * new_div
        new_div *= 10    
        orig_int %= orig_div
        orig_div /= 10
    
    return new_int * sign

if __name__=='__main__':
    test_cases=[123,-123, 4, 0, -10, 100]
    for each_test_case in test_cases:
        print each_test_case, reverse_int(each_test_case)
    
    