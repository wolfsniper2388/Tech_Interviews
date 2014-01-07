''' Given a number N and an array A in descending order 
    choose M numbers (can be repeated) from A that sum up to N, find the minimum M and the corresponding
    representation
    E.g.
        input: N=10, A=[5,3,2]
        output: 2 (10=5+5)
'''

import sys

''' get the minimum positive number in iter
    if iter are of all 0s, then return 0
    e.g. positive_min([0,4,3,2,8])=2
         positive_min([0,0,0,0])=0
'''
def positive_min(iter):
    minimum=sys.maxint
    for i in iter:
        if i>0 and i < minimum:
            minimum=i
    if minimum == sys.maxint:
        return 0
    else:
        return minimum

''' if i know min_repr(1)...min_repr(n-1), then min_repr(n) can be obtained by:
    min_repr(48)=min(min_repr(48-36), min_repr(48-24), min_repr(48-6), min_repr(48-3), min_repr(48-1)+1
                =0 if min(...)=0
    if min_repr(48-24) is the minimum then 1 means 24 would be included 
    if all the min_repr(48-i) is 0, then min_repr[48] is also 0
'''
def find_min_repr_helper(n, A, min_repr):
    if min_repr[n] != -1:
        return min_repr[n]
    prev_min=positive_min([find_min_repr_helper(n-each_num, A, min_repr) for each_num in A if n > each_num])
    # if prev_min == 0, then n cannot be the sum of any numbers in A
    if prev_min == 0:
        min_repr[n]=0
        return 0
    else:
        min_repr[n]=prev_min+1
        return prev_min+1
    

def find_min_repr(N, A):
    min_repr=[None]*(N+1)
    for i in range(1,N+1):
        if i in A:
            min_repr[i]=1
        elif i < A[-1]:
            min_repr[i]=0
        else:
            min_repr[i]=-1
    return find_min_repr_helper(N, A, min_repr)      

if __name__=='__main__':
    print find_min_repr(7, [4,2])
    print find_min_repr(10, [5,3,2])
    