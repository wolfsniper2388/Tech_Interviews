''' Q1. Two-Sum
    Given an array of integers, find two numbers such that they add up to a specific target number.
    Assume each input would have exactly one solution
    e.g
        Input: numbers=[2, 7, 11, 15], target=9
        Output: index1=1, index2=2
    
    Q2. Three-Sum 
    Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
    Find all unique triplets in the array which gives the sum of zero.
    e.g
        Input: numbers=[-10, 2, -7, -25, -3, 8, 4, 10]
        Output: index1=1, index2=2
        
    Q3. Four-Sum
    Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target?
    Find all unique quadruplets in the array which gives the sum of target.
    Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a <= b <= c <= d)
    The solution set must not contain duplicate quadruplets.
    
    
    Q4. Three-Sum nearest
    Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. 
    Return the sum of the three integers. You may assume that each input would have exactly one solution.
    e.g.
         Input: A = [-1, 2, 1, -4], and target = 1.
         Output: (-1, 1, 2), sum=2
'''

import sys

def two_sum(A, target):
    ''' B[i] = target - A[i]
        make a hash table recording A[i]
        if B[i] is in hash table, then found
        @return: indices tuple (first, second), where A[first]+A[second] == target
        @time_complexity: O(N)
    '''
    num_dict = {}
    B=[None]*len(A)
    for i,elem in enumerate(A):
        num_dict[elem]=1
        B[i] = target - elem
        if B[i] in num_dict and A[i] != B[i]:
            return (A.index(B[i]), i)
    return (-1,-1)
            
        
def three_sum_1(A):
    ''' 
        @return: number tuple (a,b,c) in A, where a+b+c == 0
        @time_complexity: O(N^2)
    '''
    triplets=[]
    for i in range(len(A)-3):
        two_sum_tuple = two_sum(A, -A[i])
        if two_sum_tuple != (-1,-1):
            first=two_sum_tuple[0]
            second=two_sum_tuple[1]
            triplet=(A[i],A[first],A[second])
            # sort and the triplet and convert back to tuple
            triplet_sorted=tuple(sorted(triplet))
            if triplet_sorted not in triplets:
                triplets.append(triplet_sorted)
    return triplets

def three_sum_2(A):
    triplets=[]
    A=sorted(A)
    # i = 0, 1, 2... last_index-2
    for i in range(len(A)-2):
        j=i+1
        k=len(A)-1
        while j < k:
            if A[i]+A[j]+A[k]<0:
                j+=1
            elif A[i]+A[j]+A[k]>0:
                k-=1
            else:
                triplets.append((A[i], A[j], A[k]))
                break
    return triplets
        

def is_distinct(a,b,c,d):
    return a!=b and a!=c and a!=d and b!=c and b!=d and c!=d


def four_sum(A):
    ''' Generate pairwise sum for each two numbers in A, and hash each pair to the sum of its two numbers
        Iterate through the hash table, use two sum technology to find the solution
        @return: number tuple (a,b,c,d) in A, where a+b+c+d == 0
        @time_complexity: O(N^2)
    '''
    quadruplets=[]
    pair_dict={}        # pair hash to sum, e.g. (2, 7) <=> 9
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            pair_dict[(A[i], A[j])]=A[i]+A[j]
    # modification of two_sum
    num_dict={}
    B={}
    for pair in pair_dict:
        pair_sum=pair_dict[pair]
        num_dict[pair_sum]=1        # pair_sum hash to 1, e.g. 9 <=> 1
        B[pair] = - pair_sum
        # if B[pair] is in num hash table
        if B[pair] in num_dict:
            # get keys from value
            candidate_pairs=[key for (key, value) in pair_dict.items() if value==B[pair]]
            for each_candidate in candidate_pairs:
                quadruplet=(each_candidate[0], each_candidate[1], pair[0], pair[1])
                # sort and the quadruplet and convert back to tuple
                quadruplet_sorted=tuple(sorted(quadruplet))
                if is_distinct(*quadruplet_sorted) and quadruplet_sorted not in quadruplets:
                    quadruplets.append(quadruplet_sorted)
    return quadruplets


def three_sum_closest(A, target): 
    triplets=[]
    A=sorted(A)
    min_difference=sys.maxint
    min_tuple=None
    # i = 0, 1, 2... last_index-2
    for i in range(len(A)-2):
        j=i+1
        k=len(A)-1
        while j < k:
            if A[i]+A[j]+A[k]<target:
                difference=target-(A[i]+A[j]+A[k])
                if difference < min_difference:
                    min_difference = difference
                    min_tuple=(A[i], A[j], A[k])
                j+=1
            elif A[i]+A[j]+A[k]>target:
                difference=A[i]+A[j]+A[k]-target
                if difference < min_difference:
                    min_difference = difference
                    min_tuple=(A[i], A[j], A[k])
                k-=1
            else:
                return (A[i], A[j], A[k])
    return min_tuple
        
    
if __name__=='__main__':
    print two_sum([9,7,11,2,3], 14)
    print three_sum_1([-10, 2, -7, -25, -3, 8, 4, 10])
    print three_sum_2([-10, 2, -7, -25, -3, 8, 4, 10])
    print four_sum([-10, 2, -9, 7, 4, 12])
    print three_sum_closest([-1, 2, 1, -4], 1)
    