'''
write a string to number function which converts string to number 
write a number to string function which converts number to string
The rule is as follows
      a - 0     aa - 26   .....   za - 676    aaa - 702
      b - 1     ab - 27   .....   zb - 677    aab - 703
      c - 2        .                 .            .
        .          .                 .            .
        .          .                 .            .
        .          .                 .            .
      z - 25    az - 51   .....   zz - 701    aaz - 727
'''

import math 
def string2Num(str):
    num=0
    for i,ch in enumerate(str):
        num+=(ord(ch)-96)*pow(26,len(str)-i-1)
    return num-1

'''n=a0+(1+a1)*26^1+(1+a2)*26^2+...+(1+ak-1)*26^(k-1)
% operation strips off the 26^1
/ operation downgrade the power of 26 by 1
'''
def num2String(num):
    string=''
    # deal with a0
    string+=chr(num%26+97)
    num=num/26
    # deal with a1...ak-1
    while num!=0:
        string+=chr((num-1)%26+97)
        num=(num-1)/26
    return string


if __name__=='__main__':
    print string2Num('aaz')
    print num2String(727)
