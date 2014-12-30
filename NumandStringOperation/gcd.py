''' calculate the greatest common divider and least common multiple of a and b
'''

def gcd(a,b):
    return a if b==0 else gcd(b, a%b)

def lcm(a,b):
    return a*b/gcd(a,b)

if __name__=='__main__':
    test_cases = [(2,4),(6,35),(24,28),(4,6)]
    for each_test_case in test_cases:
        a,b=each_test_case
        print gcd(a,b), lcm(a,b)