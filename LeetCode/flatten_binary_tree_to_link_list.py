''' Given a binary tree, flatten it to a linked list in-place.
    E.g
        Input:
         1
        / \
       2   5
      / \   \
     3   4   6
         Output:
           1
            \
             2
              \
               3
                \
                 4
                  \
                   5
                    \
                     6
    hint: If you notice carefully in the flattened tree, 
          each node's right child points to the next node of a pre-order traversal.
'''

from BinaryTree import BinaryTree

'slight modification to iterative pre-order traversal'
def flattern_bt2list(r):
    if not r:
        return
    stack = []
    stack.append(r)
    prev_node = None
    while stack:
        curr_node = stack.pop()
        if curr_node.right:
            stack.append(curr_node.right)
        if curr_node.left:
            stack.append(curr_node.left)
        if prev_node:
            prev_node.left = None
            prev_node.right = curr_node
        prev_node = curr_node
        
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
    flattern_bt2list(t.root)

    t.pre_order_print(t.root)
    print 
    t.in_order_print(t.root)