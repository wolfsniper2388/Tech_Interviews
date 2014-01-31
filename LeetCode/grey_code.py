''' The gray code is a binary numeral system where two successive values differ in only one bit.
    Given a non-negative integer n representing the total number of bits in the code, 
    print the sequence of gray code. A gray code sequence must begin with 0.
    E.g.
        Input: 3
        Output: ['000','001','011','010', '110', '111', '101', '100']
'''


def grey_code(n):
    if n==1:
        return ['0','1']
    last_result = grey_code(n-1)
    n = len(last_result)
    curr_result = last_result + last_result[::-1]
    for i in range(n):
        curr_result[i] = '0' + curr_result[i]
    for i in range(n,2*n):
        curr_result[i] = '1' + curr_result[i]
    return curr_result


if __name__=='__main__':
    for n in range(1,5):
        print n, grey_code(n)