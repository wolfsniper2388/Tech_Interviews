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
        Output: [(-10, 2, 8), (-7,-3,10)], 
        
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
    map = {}
    for i,num in enumerate(A):
        if num not in map:
            map[target-num] = num
        else:
            return (A.index(map[num]), i)
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
        

def is_valid(new_tuple, A, count_in_A):
    'check if each element in new_tuple appears exactly the same time as in A'
    count_in_tuple={}
    for elem in new_tuple:
        if elem not in count_in_tuple:
            count_in_tuple[elem]=1
        else:
            count_in_tuple[elem]+=1
    
    for elem in new_tuple:
        if count_in_tuple[elem] > count_in_A[elem]:
            return False
    return True
            
def four_sum(A, target):
    ''' Generate pairwise sum for each two numbers in A, and hash each pair to the sum of its two numbers
        Iterate through the hash table, use two sum technology to find the solution
        @return: number tuple (a,b,c,d) in A, where a+b+c+d == target
        @time_complexity: O(N^2)
    '''
    i = 0
    quadruplets=[]
    A=sorted(A)
    for i in range(len(A)):
        j = len(A)-1
        while j>i:
            left = i+1
            right = j-1
            while left < right:
                sum = A[i]+A[left]+A[right]+A[j]
                if sum > target:
                    right-=1
                elif sum < target:
                    left+=1
                else:
                  quadruplets.append([A[i],A[left],A[right],A[j]])
                  left+=1
                  right-=1
            j-=1
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
    print 'two sum', two_sum([9,7,11,2,3], 14)
    #print three_sum_1([-10, 2, -7, -25, -3, 8, 4, 10])
    print 'three sum 2', three_sum_2([-10, 2, -7, -25, -3, 8, 4, 10])
    print 'four sum',four_sum([-10, 2, -9, 7, 4, 4, -4, -4, 12], 0)
    print 'three sum closest', three_sum_closest([-1, 2, 1, -4], 1)
    