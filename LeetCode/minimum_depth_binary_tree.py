''' Given a binary tree, find its minimum depth.
    The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
'''

from BinaryTree import BinaryTree

def get_min_depth(r, depth):
    # if r is leaf or r has no left child or r has no right child, the min depth is current depth
    if not r:
        return depth-1
    
    left_min_depth = get_min_depth(r.left, depth+1)
    right_min_depth = get_min_depth(r.right, depth+1)
    
    if r.left and not r.right:
        return left_min_depth
    if not r.left and r.right:
        return right_min_depth
    return min(left_min_depth, right_min_depth)


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
    t.create_tree(pre_order, in_order)
    print get_min_depth(t.root,1)