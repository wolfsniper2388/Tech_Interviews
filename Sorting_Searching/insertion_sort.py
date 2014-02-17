''' Implement insersion sort
'''

def insertion_sort(A):
    for i in range(1, len(A)):
        tmp = A[i]
        j = i
        while j>0 and A[j-1] > tmp:
            A[j] = A[j-1]
            j-=1
        A[j] = tmp
    return A

if __name__=='__main__':
    test_cases = [[1,2,3,4], [3,8,2,5,1,4,3,6], [4,3,2,1], [3,2,2,3,3,3]]
    for each_test_case in test_cases:
        print each_test_case, insertion_sort(each_test_case)