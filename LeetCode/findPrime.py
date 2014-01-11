''' ouptut prime numbers up to n 
'''

import math

def prime_sieve(n):
    ''' is_primep[i]== True : i is prime
                       False: i is not prime
    '''
    is_prime=[True for i in range(n+1)]
    is_prime[0]=is_prime[1]=False
    # for i = 2, 3.... not exceeding sqrt(n)
    for i in range(2, int(math.floor(math.sqrt(n)))+1):
        if is_prime[i]:
            # for j = i*i, i*i+i, i*i+2i... not exceeding n
            for j in range(i*i, n+1, i):
                is_prime[j]=False
    # return a list of indices whose value is true (prime number)
    return [index for index,value in enumerate(is_prime) if value]


if __name__=='__main__':
    print prime_sieve(101)
                   