''' There are N children standing in a line. Each child is assigned a rating value.
    You are giving candies to these children subjected to the following requirements:
        Each child must have at least one candy.
        Children with a higher rating get more candies than their neighbors.
    What is the minimum candies you must give?
    E.g.
        Input: A = [5,7,3,2]
        Ouput: total_candies = 7 (1+3+2+1)
'''

# scan from left and then from right
def candy_num(A):
    # initialize all elements to be 1
    candy = [1 for i in range(len(A))]
    # i = 1,2...n-1
    for i in range(1,len(A)):
        if A[i] > A[i-1]:
            candy[i] = candy[i-1]+1
        # else candy[i] = 1, which is its intial value
    # since scan from right will skip candy[-1], we intialize total_candies to be candy[-1]
    total_candies = candy[-1]
    # i = n-2, n-3...0
    for i in range(len(A)-2, -1, -1):
        if A[i] > A[i+1]:
            candy[i] = max(candy[i], candy[i+1]+1)
        total_candies+=candy[i]
    return total_candies

if __name__=='__main__':
    test_cases = [[2,4,6,9], [5,4,3,2], [5,7,3,9,2], [3,9,2,5,4,1,7,6], [1,2,2],[5]]
    for each_test_case in test_cases:
        print each_test_case, candy_num(each_test_case)