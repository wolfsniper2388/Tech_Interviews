''' Compute the Fibonacci function
    f(0)=0
    f(1)=1
    f(n)=f(n-1)+f(n-2),    n>1
'''

from decorator_demo import cache

def fibo_1(n):
    x,y=0,1
    for i in range(n):
        x,y=y,x+y       # order is y->x, x+y->y
    return x

@cache
def fibo_2(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibo_2(n-1)+fibo_2(n-2)

#fibo_2=cache(fibo_2)

print 'Testing fibo_2',fibo_2(10)



''' Print the fibonacci series up to n
    
    fibo_3 is just a user wrapper
    it takes the user parameter and pass the initial series [] to fibo_helper
    and return the series part of the returned data
    
    fibo_helper 
    @param 
            n:        the number
            series:    the fibonacci series up to n
    @return: 
            value:    the fibonacci value of n
            series:    the fibonacci series up to n
    e.g
    parameter        return
        1            (1, [0,1])
        2            (1. [0,1,1])    # add last two elements from series above line and append to series
        3            (2, [0,1,1,2])
        4            (3, [0,1,1,2,3])
        5            (5, [0,1,1,2,3,5])
        6            (8, [0,1,1,2,3,5,8])
'''

def fibo_3(n):
    return fibo_helper(n,[])[1]

def fibo_helper(n,series):
    if n==1:
        series.append(0)
        series.append(1)
        return (1,series)
    return_value=fibo_helper(n-1,series)
    fibo_value = return_value[1][-2]+return_value[1][-1]
    series.append(fibo_value)
    return (fibo_value,series)


series=fibo_3(10)
print 'Testing fibo_3',series



def fibo_4(n, cache):
    if n==0:
        return 0
    if n==1:
        return 1
    if n in cache:
        return cache[n]
    result=fibo_4(n-1,cache)+fibo_4(n-2,cache)
    cache[n]=result
    return cache[n]


print 'Testing fibo_4', fibo_4(10, {})


