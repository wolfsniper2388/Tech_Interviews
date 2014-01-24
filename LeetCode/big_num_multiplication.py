''' Given two numbers represented as strings, return multiplication of the numbers as a string.
    Note: The numbers can be arbitrarily large and are non-negative.
'''


''' Idea: Karatsuba algorithm
    x = x1 | x0    so that x = x1 * 10^m + x0
    y = y1 | y0    so that y = y1 * 10^m + y0
    let z2 = x1*y1
        z1 = (x1+x0)(y1+y0)
        z0 = x0*y0
    x*y = z2*10^2m + (z1-z0-z2)*10^m + z0
'''
def multiply(x, y):
    max_size = max(len(x), len(y))
    x = ''.join(['0' for i in range(len(x), max_size)])+x
    y = ''.join(['0' for i in range(len(y), max_size)])+y
    if len(x) == 1  or len(y) == 1:
        return int(x) * int(y)
    
    m0 = (max_size+1)/2
    m1 = max_size/2
    x1 = x[:m0]
    x0 = x[m0:]
    y1 = y[:m0]
    y0 = y[m0:]
    z2 = multiply (x1,y1)
    z1 = multiply (str(int(x1)+int(x0)), str(int(y1)+int(y0)))
    z0 = multiply (x0, y0)
    return z2*pow(10, 2*m1) + (z1-z2-z0)*pow(10, m1) + z0

if __name__=='__main__':
    test_cases = [('123','456'), ('45791273','2688130'), ('123456789','987654321')]
    for each_test_case in test_cases:
        x,y = each_test_case
        print x, y, multiply(x,y), 'Expected:', int(x)*int(y)