''' find the maximum sum of nodes value from root to leaf in a binary tree
'''

from BinaryTree import BinaryTree
import sys


def path_max_sum(r):
    max_sum = [-sys.maxint]
    max_sum_helper(r, 0, max_sum)
    return max_sum[0]

def max_sum_helper(r, curr_sum, max_sum):
    if not r:
        return
    curr_sum+=r.data
    if not r.left and not r.right:
        max_sum[0] = max(max_sum[0], curr_sum)
        return
    max_sum_helper(r.left, curr_sum, max_sum)
    max_sum_helper(r.right, curr_sum, max_sum)


if __name__=='__main__':
    ''' The tree is:
                     1
                   /   \ 
                 2      3
                / \    / \
               4   5  8   9
                  / \    / \
                 6   7  10  11
                /
               12
    '''
    t=BinaryTree()
    pre_order=[1,2,4,5,6,12,7,3,8,9,10,11]
    in_order=[4,2,12,6,5,7,1,8,3,10,9,11]
    root=t.create_tree(pre_order, in_order)
    print path_max_sum(root)
    