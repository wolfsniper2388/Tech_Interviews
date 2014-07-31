''' Given 2 binary trees T1 and T2, check if T2 is a subtree of T1
'''
from BinaryTree import BinaryTree



def is_subtree(r1,r2):
    if not r1:
        return False
    if r1.data == r2.data:
        return are_identical(r1,r2)
    return is_subtree(r1.left, r2) or is_subtree(r1.right, r2)

def are_identical(r1,r2):
    if not r1 and not r2:
        return True
    if not r1 or not r2:
        return False
    if r1.data!=r2.data:
       return False
    return are_identical(r1.left, r2.left) and are_identical(r1.right, r2.right)

if __name__=='__main__':
    ''' T1 is:
                     1
                   /   \ 
                 2      3
                / \    / \
               4   5  8   9
                  / \    / \
                 6   7  10  11
                /
               12
               
               
        T2 is :
                     3
                    /  \
                   8    9
                       / \
                     10  11
    '''
    t1=BinaryTree()
    pre_order=[1,2,4,5,6,12,7,3,8,9,10,11]
    in_order=[4,2,12,6,5,7,1,8,3,10,9,11]
    r1=t1.create_tree(pre_order, in_order)
    
    t2=BinaryTree()
    pre_order=[3,8,9,10,11]
    in_order=[8,3,10,9,11]
    r2=t2.create_tree(pre_order, in_order)
    print is_subtree(r1,r2)