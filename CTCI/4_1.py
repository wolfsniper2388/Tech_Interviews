''' Implement a function if a binary tree is balanced. A balanced tree is defined to be a tree such that the heights
of the two subtrees of any node never differ by more than 1
'''

from BinaryTree import BinaryTree

# return -1 if the tree is not balanced
# or return the height of the tree
def check_height(r):
    if not r:
        return 0
    left_height=check_height(r.left)
    right_height=check_height(r.right)
    if left_height==-1:
        return -1
    if right_height==-1:
        return -1
    if abs(left_height-right_height)>1:
        return -1
    else:
        return max(left_height, right_height)+1

def is_balanced(r):
    if check_height(r)==-1:
        return False
    else:
        return True


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
    t=BinaryTree();
    pre_order=[1,2,4,5,6,12,7,3,8,9,10,11]
    in_order=[4,2,12,6,5,7,1,8,3,10,9,11]
    root=t.create_tree(pre_order, in_order)
    print is_balanced(root)
    