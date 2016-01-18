'''

'''
from BinarySearchTree import *

def midOrder(root, k, result, cnt):
    if not root:
        return
    midOrder(root.left, k, result, cnt)
    if cnt[0] == k:
        result.append(root)
    cnt[0]+=1
    midOrder(root.right, k, result, cnt)
    
def kthSmallest(root, k):
    """
    :type root: TreeNode
    :type k: int
    :rtype: int
    """
    result = []
    midOrder(root, k, result,[1])
    return result[0].data

if __name__ == '__main__':
    t=BinarySearchTree()
    ''' The tree is :
                        20
                     /      \
                  10          40
                /    \       /  \
               3       17   35    73
              /  \     / \          \
             1    7  15  18         89
             \    /  /
              2  5  11
                / \   \
               4   6   12
    
    '''
    a=[20,10,40,3,17,35,73,1,7,15,18,89,2,5,11,4,6,12]
    for key in a:
        t.add_node(key)
    r=t.root
    print t.level_order_print(r)
    print kthSmallest(r, 10)
    

