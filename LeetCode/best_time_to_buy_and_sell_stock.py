''' Q1. stock price, one transaction
    Given an array A, maximize: A[i]-A[j], where i>j
    
    Q2. stock price, multiple transaction (one transaction a time)
    Given an array A. maximize: sigma A[s[j]] - A[b[j]] where 0<=b[j] < s[j]<=len(A)-1 and b[j+1] > s[j]
    b[i] stands for the index of ith buying, s[i] ith selling
    
    Q3. stock price, at most two transaction (one transaction a time)
    Given an array A, maximize A[s1]-A[b1] + A[s2]- A[b2] where 0 <= b1<s1<b2<s2<=len(A)-1
    
'''
import sys

def buy_sell_stock_q1(A):
    if not A:
        return 
    min_index = max_diff = start = end = 0
    for i in range(len(A)):
        # record index of current minimum
        if A[i] < A[min_index]:
            min_index = i
        diff = A[i] - A[min_index]
        if diff > max_diff:
            max_diff = diff
            start = min_index
            end = i
    return (A[start],A[end])

''' Greedy
'''
def buy_sell_stock_q2(A):
    curr_min_index=i=0
    total_profit = 0
    max_diff = 0
    A.append(-sys.maxint)
    for i in range(len(A)):
        diff = A[i] - A[curr_min_index]
        if diff < max_diff:
            # A[i-1] is the current sell price, A[curr_min_index] is the current buy price
            total_profit += A[i-1] - A[curr_min_index]
            # update curr_min_index to i
            curr_min_index = i
            max_diff = 0
        else:
            max_diff = diff    
    A.pop()     
    return total_profit

''' scan from left, then scan from right
'''
def buy_sell_stock_q3(A):
    if not A:
        return 0
    curr_max_profit_left = [0 for i in range(len(A))]
    curr_min = A[0]
    for i in range(1,len(A)):
        curr_min = min(curr_min, A[i])
        curr_max_profit_left[i] = max(curr_max_profit_left[i-1], A[i] - curr_min)
    curr_max = A[-1]
    curr_max_profit_right = 0
    total_profit = 0
    for i in range(len(A)-2, -1, -1):
        curr_max = max(curr_max, A[i])
        curr_max_profit_right = max(curr_max_profit_right, curr_max - A[i])
        total_profit = max(total_profit, curr_max_profit_right + curr_max_profit_left[i])
    return total_profit
        
    
    
if __name__=='__main__':
    test_cases = [[5,4,3,2,9,6,0,8],[3,1,5,6,2,9,-1,2,9,8], [3,5,1,2,9,8,0,7,4], []]
    
    for each_test_case in test_cases:
        A = each_test_case
        print 'Q1'
        print A, buy_sell_stock_q1(A)
        print 'Q2'
        print A, buy_sell_stock_q2(A)
        print 'Q3'
        print A, buy_sell_stock_q3(A)
