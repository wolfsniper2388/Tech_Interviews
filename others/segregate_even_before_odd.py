''' Riverbed phone interview:
    Given an array, reorder the array in place so that all the even numbers come before odd numbers, original order doesn't have to be preserved
    E.g
        Input: [3,6,4,9,11,2]
        Output: [2,6,4,9,11,3]
'''

def segregate_1(A):
    i=0;
    j=len(A)-1
    while i < j:
        while i<j and A[i] % 2 == 0:
            i+=1
        while i<j and A[j] %2 ==1:
            j-=1
        if i<j:
            A[i],A[j] = A[j],A[i]
    return A

def cmp(l, r):
    if l%2==0 and r%2==1:
        return 0
    elif l%2==1 and r%2==0:
        return 1
    else:
        return 0 if l<=r else 1
def segregate_2(A):
    A = sorted(A, cmp)
    return A

if __name__=='__main__':
    test_cases = [[3,6,4,9,11,2],[3,8,12,5,9,21,6,10]]
    for each_test_case in test_cases:
        print each_test_case,segregate_2(each_test_case)