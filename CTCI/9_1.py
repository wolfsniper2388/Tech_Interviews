''' how many possible ways can the child run up the stairs with n staircases
    while he can hop either 1 staircase, 2 staircases or 3 staircases at one time
'''

N=100
cache=[0 for x in range(N)]
def staircase(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    if cache[n]!=0:
        return cache[n]
    cache[n]=staircase(n-1)+staircase(n-2)+staircase(n-3)
    return cache[n]

if __name__=='__main__':
    print staircase(10)