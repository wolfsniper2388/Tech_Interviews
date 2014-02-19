''' Given two binary strings, return their sum (also a binary string).
    E.g.
        Input: '111', '11'
        Output: '1010'
'''

def add_binary(A, B):
    i = len(A)-1
    j = len(B)-1
    carry =0
    sum = 0
    result = []
    while i>=0 or j>=0 or carry:
        A_val = int(A[i]) if i>=0 else 0
        B_val = int(B[j]) if j>=0 else 0
        sum = A_val+B_val+carry
        carry = sum/2
        sum = sum%2
        result.append(str(sum))
        i-=1 
        j-=1 
    return ''.join(reversed(result))
        
        
if __name__=='__main__':
    test_cases = [('1111','1'), ('101', '1011'), ('111','11'), 
                  ('11110011001011110111110001010000111110011110101100011111010010001000001101111001000111', 
                   '111001011011111010001001111001100000101010000101100010101100010010010011011000')]
    for each_test_case in test_cases:
        A,B = each_test_case
        print A,B, add_binary(A,B)