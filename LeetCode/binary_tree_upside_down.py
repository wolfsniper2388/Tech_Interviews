''' 
Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the same parent node) or empty, flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes. Return the new root.

For example:
Given a binary tree {1,2,3,4,5},
    1
   / \
  2   3
 / \
4   5
return the root of the binary tree [4,5,2,#,#,3,1].
   4
  / \
 5   2
    / \
   3   1  
'''
from BinaryTree import *
def binary_tree_upside_down(root):
    dummy_root = TreeNode(0)
    cousin = None
    while root:
        # record left and right
        left_child = root.left
        right_child = root.right
        # insert under dummy_root's right
        root.right = dummy_root.right
        dummy_root.right = root
        # connect left
        root.left = cousin
        # update cousin and root itself
        cousin = right_child
        root = left_child
    return dummy_root.right


if __name__=='__main__':
    t1 = BinaryTree()
    pre_order = [1,2,4,5,3]
    in_order =  [4,2,5,1,3]
    r1 = t1.create_tree(pre_order, in_order)
    r2 = binary_tree_upside_down(r1)
    t2 = BinaryTree()
    t2.clone_tree(r2)
    t2.pre_order_print(r2)
    print
    t2.in_order_print(r2)