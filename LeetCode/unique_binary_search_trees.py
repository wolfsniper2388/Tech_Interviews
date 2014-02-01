''' Q1.
    Given n, how many structurally unique BST's (binary search trees) that store values 1...n?
    E.g.
        Input: 3
        Output: 5

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''


''' if n is odd then
    ways[n] = (ways[n-1]*ways[0]+ways[n-2]*ways[1]+...+ways[n/2+1]*ways[n/2-1])*2 + ways[n/2]*ways[n/2]
    if n is even then
    ways[n] = (ways[n-1]*ways[0]+ways[n-2]*ways[1]+...+ways[n/2]*ways[n/2-1])*2
'''
# bottom-up solution
def unique_bst_num_1(n):
    ways = [0 for i in range(n+1)]
    ways[0] = 1
    ways[1] = 1
    for i in range(2,n+1):
        # i is odd
        if i % 2 == 1:
            for j in range(i/2):
                ways[i] += ways[j]*ways[i-1-j]*2
            ways[i]+=ways[i/2]*ways[i/2]
        # i is even
        else:
            for j in range(i/2):
                ways[i] += ways[j]*ways[i-1-j]*2
    return ways[n]

#up-down solution
#from decorator_demo import cache
#@cache
def unique_bst_num_2(n, ways):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if ways[n]!=0:
        return ways[n]
    tmp = 0 
    if n % 2 == 1:
        for j in range(n/2):
            tmp += unique_bst_num_2(j, ways)*unique_bst_num_2(n-1-j, ways)*2
        tmp += unique_bst_num_2(n/2,ways)*unique_bst_num_2(n/2,ways)
    else:
        for j in range(n/2):
            tmp += unique_bst_num_2(j,ways)*unique_bst_num_2(n-1-j,ways)*2
    ways[n] = tmp
    return ways[n]
        

if __name__=='__main__':
    test_cases = range(1,8)
    for each_test_case in test_cases:
        print each_test_case, unique_bst_num_1(each_test_case),unique_bst_num_2(each_test_case, [0 for i in range(each_test_case+1)])