'''
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return '0.5'
Given numerator = 2, denominator = 1, return '2'
Given numerator = 2, denominator = 3, return 0.(6)
Given numerator = 1, denominator = 7, return 0.(142857)

'''

def fraction_to_decimal(num, denom):
    assert (denom != 0)
    
    if num % denom == 0:
        return num / denom
    
    sign = 1
    if num > 0 and denom < 0:
        denom = -denom
        sign = -1
    elif num < 0 and denom > 0:
        num = -num
        sign = -1
    
    result = [str(num / denom)] if sign == 1 else ['-'+str(num / denom)]
    
    num = num % denom
    remainder_table = {num:0}
    while num:
        quotient = num * 10 / denom
        remainder = num * 10 % denom
        result.append(str(quotient))
        if remainder in  remainder_table:
            break
        remainder_table[remainder] = len(result)-1
        num = remainder
    
    index = remainder_table[remainder]
    if num != 0:
        result.insert(index+1, '(')
        result.append(')')
    result.insert(1, '.')
    return ''.join(result)

if __name__=='__main__':
    test_cases = [(1,333), (10,11), (1,6), (7,3), (6,2), (1,7), (3,-2), (7,-3), (1, 99), (3,20), (0,3)]
    for each_test_case in test_cases:
        num, denom = each_test_case
        print num, denom, fraction_to_decimal(num, denom)
    