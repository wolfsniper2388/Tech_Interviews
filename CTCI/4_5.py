''' Check if a binary tree is a binary search tree
'''

from BinaryTree import BinaryTree
import sys

def is_bst(r):
    return is_bst_helper(r,-sys.maxint, sys.maxint)

''' suppose r is 20, then r.data should be in range (-maxint, maxint)
    when branch left, r.data (10) should be in range (-maxint, 20)
    when branch right, r.data (30) shoudl be in range (20, maxint)
    So when branch left, modify the maximum, when branch right, modify the minimum 
'''
def is_bst_helper(r, minimum, maximum):
    if not r: 
        return True
    if r.data<minimum or r.data>maximum:
        return False
    if not is_bst_helper(r.left, minimum, r.data) or not is_bst_helper(r.right, r.data, maximum):
        return False
    return True
    
if __name__=='__main__':
    ''' The tree is:
                     20
                   /   \ 
                 10     30
                / \    
               5   15  
              / \   \
             3   7   17  
                
               
    '''
    t=BinaryTree();
    pre_order=[20,10,5,3,7,15,17,30]
    in_order=[3,5,7,10,15,17,20,30]
    root=t.create_tree(pre_order, in_order)
    print is_bst(root)
    
    