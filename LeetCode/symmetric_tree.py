''' Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
    E.g. 
        Input: 
                1
               / \
              2   2
             / \ / \
            3  4 4  3
        Output:
            True
        Input:
                1
               / \
              2   2
               \   \
               3    3
'''
from BinaryTree import BinaryTree

def is_symmetric(r):
    if r:
        return is_symmetric_helper(r.left, r.right)
    else:
        return False

def is_symmetric_helper(r1,r2):
    if not r1 and not r2:
        return True
    if r1 and r2:
        if r1.data == r2.data:
            return is_symmetric_helper(r1.left, r2.right) and is_symmetric_helper(r1.right, r2.left)
    return False


if __name__=='__main__':
    test_cases = [([1,2,3,4,2,4,3],[3,2,4,1,4,2,3]), ([1,2,3,2,3],[3,2,1,3,2])]
    for each_test_case in test_cases:
        pre_order, in_order = each_test_case
        t=BinaryTree()
        t.create_tree(pre_order, in_order)
        print is_symmetric(t.root)