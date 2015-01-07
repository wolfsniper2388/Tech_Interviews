''' Given an array of size n, find the majority element. The majority element is the element that appears strictly more than [n/2] times.

    You may assume that the array is non-empty
    
    return None if there is no majority elements
           majority elements if there is one
'''

def majority_element(num):
    majority_index = 0
    count = 1
    n = len(num)
    for i in range(1,n):
        if num[i] == num[majority_index]:
            count += 1
        else:
            count -= 1
        if count == 0:
            majority_index = i
            count = 1
    count = 0
    for i in range(n):
        if num[i] == num[majority_index]:
            count += 1
    return num[majority_index] if count>len(num)/2 else None
        

if __name__=='__main__':
    test_cases = [[1,2,2,3,3,3], [1,2,2,3,3], [1,2,3,4,5], [1,1,7,1,9,1], [2,1,5,4,1,1,7,1,1]]
    for each_test_case in test_cases:
        print each_test_case, majority_element(each_test_case)