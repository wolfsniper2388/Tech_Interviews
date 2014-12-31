''' Given a binary tree, get all the paths from root to leaf
'''

from BinaryTree import BinaryTree
from copy import deepcopy

def all_paths(r, curr_path, paths):
    if not r:
        return
    curr_path.append(r.data)
    if not r.left and not r.right:
        paths.append(deepcopy(curr_path))
        curr_path.pop()
    
    else:
        
        all_paths(r.left, curr_path, paths)
        all_paths(r.right, curr_path, paths)
        curr_path.pop()

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
    curr_path=[]
    paths=[]
    all_paths(root, curr_path, paths)
    print paths