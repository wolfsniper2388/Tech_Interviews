''' Given an array of integers, find two numbers such that they add up to a specific target number.
    Assume each input would have exactly one solution
    e.g
        Input: numbers=[2, 7, 11, 15], target=9
        Output: index1=1, index2=2

'''

def two_sum(A, target):
    ''' B[i] = target - A[i]
        make a hash table recording A[i]
        if B[i] is in hash table, then found
    '''
    num_dict = {}
    B=[None]*len(A)
    for i,elem in enumerate(A):
        num_dict[elem]=1
        B[i] = target - elem
        if B[i] in num_dict and A[i] != B[i]:
            return (A.index(B[i]), i)
    return (-1,-1)
            
        


if __name__=='__main__':
    print two_sum([9,7,11,2,3], 14)