''' Given an array of integers, and two integer thresholds: t1, t2 (t1<t2), regroup the array such that all the numbers < t1 goes before t1,
all the numbers >=t1 and <=t2 goes after t1 and before t2, all the numbers >t2 goes after t2, the original order can be broken

e.g.
    Input: A= [5,10,15,3,55,28,34,1,2,20], t1 = 15, t2 = 28
    Output: A = [5, 10, 3, 1, 2, 15, 20 , 28, 34, 55]
'''


def partition_into_three(A, t1, t2):
    i = 0
    j = len(A)-1
    tmp=-1
    while i < j:
        if A[i] < t1:
            i+=1
        else:
            if A[j] < t1:
                A[i], A[j] = A[j], A[i]
            if A[j] == t1:
                tmp = j
            j-=1
    if tmp != -1:
        A[tmp] = A[i]
        A[i] = t1
        
    j = len(A)-1
    while i < j:
        if A[i] < t2:
            i+=1
        else:
            if A[j] < t2:
                A[i], A[j] = A[j], A[i]
            if A[j] == t2:
                tmp = j
            j-=1
    if tmp != -1:
        A[tmp] = A[i]
        A[i] = t2
    return A

if __name__ == '__main__':
    test_cases = [([5,10,15,3,55,28,34,1,2,20], 15,28),([2,1,3] , 1,3), ([6,8,1,3,9,12,2,7], 4, 11)]
    for each_test_case in test_cases:
        A,t1,t2 = each_test_case
        print A,t1,t2, partition_into_three(A,t1,t2)
                    