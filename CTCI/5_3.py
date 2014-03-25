''' Given a positive number n, find the next smallest number and previous largest number both with the same 1s in n
'''


from BitOperation import *

def get_next_smallest(n):
    tmp=n
    
    ''' let p be the position of the rightmost non-trailing zero
        let c0 be the number of trailing 0s to the right of p
        let c1 be the number of 1s to the right of p
        e.g.
        n=11011001111100
        c0=2, c1=5, p=7, notice that p==c0+c1 is always true 
    '''
    c0=c1=0
    while (tmp & 1)==0 and tmp != 0:
        c0+=1
        tmp = tmp>>1
    while (tmp & 1) == 1:
        c1+=1
        tmp = tmp>>1
    if c0+c1 == 32 or c0+c1==0:
        return -1
    p=c0+c1
    # set bit at p
    n=set_bit(n,p)
    # clear bits from 0 to p-1
    n = clear_bits_right(n,p)
    # set bits at from 0 to c1-2
    n = n | (1<<(c1-1)) -1
    return bin(n)

def get_prev_largest(n):
    tmp=n
    ''' let c1 be the trailing 1s to the right of p
        let c0 be the number of 0s to the right of p
    '''
    c0=c1=0
    while tmp & 1 == 1:
        c1+=1
        tmp = tmp>>1
    # n is like 00...001111
    if tmp == 0:
        return -1
    while tmp & 1 == 0:
        c0+=1
        tmp = tmp>>1
    p = c0+c1
    # clear bits to the right of p+1
    n=clear_bits_right(n, p+1)
    # generate (c1+1) ones
    mask = (1<<(c1+1))-1
    n = n | mask<<(c0-1)
    return bin(n)
    
    

if __name__=='__main__':
    test_cases = [0b11011001111100,0b1010,0b10011110000011,0b0]
    for each_test_case in test_cases:
        print 'the smallest number larget than', bin(each_test_case), 'is' ,get_next_smallest(each_test_case)
        print 'the largetest number smaller than', bin(each_test_case), 'is' ,get_prev_largest(each_test_case)
        