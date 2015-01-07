'''
Given two numbers represented as strings, return multiplication of the numbers as a string.

Note: The numbers can be arbitrarily large and are non-negative.
'''

def multiply_strings(s1,s2):
    s1 = s1[::-1]
    s2 = s2[::-1]
    m = len(s1)
    n = len(s2)
    result = ['0'] * (m+n+1)
    for i in range(m):
        carry = 0
        num1 = int(s1[i])
        for j in range(n):
            num2 = int(s2[j])
            exist = int(result[i+j])
            product = num1*num2+carry+exist
            result[i+j] = str(product % 10)
            carry = product/10
        if carry > 0:
            result[i+n] = str(carry)
    result = result[::-1]
    i = 0
    while i < m+n+1 and result[i] == '0':
        i += 1
    return ''.join(result[i:]) if i < m+n+1 else '0'
        


if __name__=='__main__':
    test_cases = [('99','99'), ('23456','29183764'),('1','234'),('102','4098707'),('0','0')]
    for each_test_case in test_cases:
        s1,s2 = each_test_case
        print s1,s2,multiply_strings(s1,s2)
            
    