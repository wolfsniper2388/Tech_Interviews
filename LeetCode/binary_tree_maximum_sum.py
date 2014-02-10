''' Given a binary tree, find the maximum path sum.
    The path may start and end at any node in the tree.
    E.g
    Input:
         -1
        /  \ 
       1     9
      / \   / \ 
     23  2 7   6
        /
       24  
    Output:
        50 (23+1+2+24)
    
''' 
from BinaryTree import BinaryTree
import sys

def max_path_sum(r):
    max_sum = [-sys.maxint]
    # pass in max_sum as a list to modify it's value in recursion
    max_path_sum_helper(r, max_sum)
    return max_sum[0]

def max_path_sum_helper(r, max_sum):
    if not r:
        return 0
    # get left and right subtrees' max sum path
    left_max = max(0,max_path_sum_helper(r.left, max_sum))
    right_max = max(0,max_path_sum_helper(r.right, max_sum))
    # update max_sum
    max_sum[0] = max(max_sum[0], r.data+left_max+right_max)
    # can only return one subtree path, return the larger one
    return max(r.data+left_max, r.data+right_max)


if __name__=='__main__':
    t=BinaryTree()
    pre_order=[-1,1,23,2,24,9,7,6]
    in_order=[23,1,24,2,-1,7,9,6]
    t.create_tree(pre_order, in_order)
    t.in_order_print(t.root)
    print
    print max_path_sum(t.root)    