'''
Q1: 
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

Q2:

'''


from BinaryTree import *

def has_path_sum(root, target):
    return has_path_sum_helper(root, target, 0)
        
def has_path_sum_helper(root, target, curr_sum):
    if not root:
        return False
    curr_sum += root.data
        
    if not root.left and not root.right and curr_sum == target:
        return True
    return has_path_sum_helper(root.left, target, curr_sum) or has_path_sum_helper(root.right, target, curr_sum)

if __name__=='__main__':
    t = BinaryTree()
    pre_order = [5,4,11,7,2,8,13,4,1]
    in_order = [7,11,2,4,5,13,8,4,1]
    t.create_tree(pre_order, in_order, 'pre_in')
    print has_path_sum(t.root, 22)