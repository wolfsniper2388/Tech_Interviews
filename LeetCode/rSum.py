''' Q1. Given an array of integers, find two numbers such that they add up to a specific target number.
    Assume each input would have exactly one solution
    e.g
        Input: numbers=[2, 7, 11, 15], target=9
        Output: index1=1, index2=2
    
    Q2. Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
    Find all unique triplets in the array which gives the sum of zero.
    e.g
        Input: numbers=[-10, 2, -7, -25, -3, 8, 4, 10]
        Output: index1=1, index2=2
'''

def two_sum(A, target, start):
    ''' B[i] = target - A[i]
        make a hash table recording A[i]
        if B[i] is in hash table, then found
    '''
    num_dict = {}
    B=[None]*len(A)
    for i,elem in enumerate(A[start:]):
        num_dict[elem]=1
        B[i] = target - elem
        if B[i] in num_dict and A[i+start] != B[i]:
            return (A.index(B[i]), i+start)
    return (-1,-1)
            
        
def three_sum(A):
    triplets=[]
    for i in range(len(A)-3):
        two_sum_tuple = two_sum(A, -A[i], i+1)
        if two_sum_tuple != (-1,-1):
            triplets.append((i,)+two_sum_tuple)
    return triplets


def distinct(a,b,c,d):
    return a!=b and a!=c and a!=d and b!=c and b!=d and c!=d

def is_repeated_tuple():

def four_sum(A):
    quadruplets=[]
    pair_hash={}
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            pair_hash[(A[i], A[j])]=A[i]+A[j]
    # modification of two_sum
    num_dict={}
    B={}
    for pair in pair_hash:
        pair_sum=pair_hash[pair]
        num_dict[pair_sum]=1
        B[pair] = - pair_sum
        if B[pair] in num_dict:
            candidate_pairs=[key for (key, value) in pair_hash.items() if value==B[pair]]
            for each_candidate in candidate_pairs:
                if distinct(each_candidate[0], each_candidate[1], pair[0], pair[1]):
                    quadruplets.append((each_candidate[0], each_candidate[1], pair[0], pair[1]))
    
    return quadruplets
            
    
if __name__=='__main__':
    print two_sum([9,7,11,2,3], 14, 1)
    print three_sum([-10, 2, -7, -25, -3, 8, 4, 10])
    print four_sum([-10, 2, -9, 7, 4, 12])