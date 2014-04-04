''' Given a number n and string s, rotate the string to left by n
    Example:
        input:
            string= 'abcdef'
            n=4
    output:
            string= 'efabcd'
'''
from inversion import invert_char

''' Left rotate string s by n  
'''

def rotate_string(s, n):
    n = n % len(s)
    # 'abcd' -> 'dcba'
    s1=invert_char(s[:n])
    # 'ef' -> 'fe'
    s2=invert_char(s[n:])
    # 'dcbafe' -> 'efabcd'
    return invert_char(s1+s2)

if __name__=='__main__':
    print rotate_string('abcdef', 8)