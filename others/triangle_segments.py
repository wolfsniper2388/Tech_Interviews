''' Given a list of numbers that are candidates of triangle sides
    find all possible triple-let that can form a triangle
    E.g.
        Input: [2,3,5,6]
        Output: [(2,5,6),(3,5,6)]
'''

def binary_search(A, target, low, high):
    
    while low<=high:
        mid=low+(high-low)/2
        if A[mid] == target:
            return mid
        elif A[mid] < target:
            low=mid+1
        else:
            high=mid-1
    return low

def form_triangle(A):
    if len(A)<3:
        return []
    results=[]
    for i in range(len(A)):
        for j in range(i+1,len(A)-1):
            split = binary_search(A, A[i]+A[j], j+1, len(A)-1)
            for k in range(j+1, split):
                results.append((A[i],A[j],A[k]))
    return results


if __name__=='__main__':
    test_cases=[[5,6,8,10,11,14],[1,2],[1,2,3],[3,4,5],[2,4,5,6,9],[2,3,5,6]]
    for each_test_case in test_cases:
        print each_test_case, form_triangle(each_test_case)
                