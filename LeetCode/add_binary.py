''' Given two binary strings, return their sum (also a binary string).
    E.g.
        Input: '111', '11'
        Output: '1010'
'''

def add_binary(A, B):
    # ensure A's length is always larger than or equal to B's length
    if len(A) < len(B):
        A,B = B,A
    i = len(A)-1
    j = len(B)-1
    result_bin_list = []
    result_digit = 0
    carry = 0
    while i>=0 and j>=0:
        result_digit = int(A[i]) ^ int(B[j]) ^ carry
        carry = (int(A[i]) and int(B[j])) or (carry & (int(A[i]) ^ int(B[j])))
        result_bin_list.append(str(result_digit))
        i-=1
        j-=1
    while i >= 0:
        result_digit = int(A[i]) ^  carry
        carry = carry & int(A[i])
        result_bin_list.append(str(result_digit))
        i-=1
    if carry:
        result_bin_list.append(str(carry))
    return ''.join(result_bin_list)[::-1]

if __name__=='__main__':
    test_cases = [('1111','1'), ('101', '1011'), ('111','11'), 
                  ('11110011001011110111110001010000111110011110101100011111010010001000001101111001000111', 
                   '111001011011111010001001111001100000101010000101100010101100010010010011011000')]
    for each_test_case in test_cases:
        A,B = each_test_case
        print A,B, add_binary(A,B)