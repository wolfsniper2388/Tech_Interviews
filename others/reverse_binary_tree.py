''' Given a binary tree such that each non-leaf node only has leaf node as its left child, reverse the tree such that the rightmost child becomes the root and root becomes the leftmost child, each
    left leaf child becomes right leaf child
e.g.
    Input:
                    A
                   / \
                  B   C
                     / \
                    D   E
                       / \
                      F   G
                         /
                        H
    Output:
                    G
                   / \
                  E   H
                 / \
                C   F
               / \
              A   D
               \
                B
'''  

from BinaryTree import TreeNode, BinaryTree

def pre_order_traversal(root):
    if root:
        print root.data,
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)

def in_order_traversal(root):
    if root:
        
        in_order_traversal(root.left)
        print root.data,
        in_order_traversal(root.right)

def reverse_binary_tree(root):
    dummy_root = TreeNode(0)
    while root:
        right_child = root.right
        left_child = root.left
        root.left = dummy_root.left
        dummy_root.left = root
        root.right = left_child
        root = right_child
    return dummy_root.left

if __name__=='__main__':
    '''
    The Tree is:
                    A
                   / \
                  B   C
                     / \
                    D   E
                       / \
                      F   G
                         /
                        H
    '''
    t=BinaryTree()
    pre_order=['A','B','C','D','E','F','G','H']
    in_order=['B','A','D','C','F','E','H','G']
    root=t.create_tree(pre_order, in_order)
    new_root = reverse_binary_tree(root)
    pre_order_traversal(new_root)
    print
    in_order_traversal(new_root)
         