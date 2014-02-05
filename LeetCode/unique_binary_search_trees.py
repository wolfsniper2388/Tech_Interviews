''' Q1.
    Given n, how many structurally unique BSTs (binary search trees) that store values 1...n?
    E.g.
        Input: 3
        Output: 5

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
   
   Q2.
   Instead of outputting numbers of unique BSTs, print out the structure
   E.g
       Input: 3
       Output:
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
def unique_bst_num_q1_1(n):
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
def unique_bst_num_q1_2(n, ways):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if ways[n]!=0:
        return ways[n]
    tmp = 0 
    if n % 2 == 1:
        for j in range(n/2):
            tmp += unique_bst_num_q1_2(j, ways)*unique_bst_num_q1_2(n-1-j, ways)*2
        tmp += unique_bst_num_q1_2(n/2,ways)*unique_bst_num_q1_2(n/2,ways)
    else:
        for j in range(n/2):
            tmp += unique_bst_num_q1_2(j,ways)*unique_bst_num_q1_2(n-1-j,ways)*2
    ways[n] = tmp
    return ways[n]

from BinaryTree import *

def unique_bst_q2(n):
    return unique_bst_q2_helper(1,n)



''' for example n=5, i=3 (current root is 3)
    find all possible left subtrees using recursion:
     2         1
    /    and    \
   1             2
    and all possible right subtrees using recursion:
     4         5
    /    and    \
   5             4
   then connect the current root (3) to each left subtree and right subtree
      3            3            3            3
     / \          / \          / \          /  \
    2   4        2   5        1   4        1    5 
   /    \       /   /          \   \       \   /
  1      5     1   4            2   5       2 4
'''
def unique_bst_q2_helper(start, end):
    bsts=[]
    if start > end:
        bsts.append(BinaryTree(None))
        return bsts
    # current root is i
    for i in range(start, end+1):
        # generate all left_subtrees, will return a list of all possible left subtrees
        left_subtrees = unique_bst_q2_helper(start, i-1)
        # generate all right_subtrees, will return a list of all possible right subtrees
        right_subtrees = unique_bst_q2_helper(i+1, end)
    
        # for each left subtree and each right subtree
        for j in range(len(left_subtrees)):
            for k in range(len(right_subtrees)):
                # current root is i
                curr_root = TreeNode(i)
                # connect curr_root to left subtree's root and right subtree's root 
                curr_root.left = left_subtrees[j].root
                curr_root.right = right_subtrees[k].root
                # create a new bst using curr_root as root
                curr_bst = BinaryTree(curr_root)
                # append to the result
                bsts.append(curr_bst)
    return bsts
        
        
if __name__=='__main__':
    'Q1'
    test_cases = range(1,8)
    for each_test_case in test_cases:
        print each_test_case, unique_bst_num_q1_1(each_test_case),unique_bst_num_q1_2(each_test_case, [0 for i in range(each_test_case+1)])

    'Q2'
    for bst in unique_bst_q2(4):
        bst.pre_order_print(bst.root)
        print