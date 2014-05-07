from __future__ import division
from collections import deque

import sys
print sys.maxint

a1=int(0b0000111111)
a2=int('101110', 2)
a3=0b0011
print bin(a3<<2)
print a1,a2

print (~0<<1) & 0b1010
print bin(~(1 << 6 -1))
print (~((1 << 6) -1))

a=5
b=a
a+=1
print a,b


a=[1,2,3]
b=a
a=None
print b
a=set(['ab','ba'])
print a
for item in a:
    print item
    
s=set(['a','a','b'])
print s
s.remove('a')
print s

s='abc'
s= '#'.join(s)
s='#'+s+'#'
print s

a=5
b=5
print id(a), id(b)