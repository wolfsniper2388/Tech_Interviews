''' Find the next node in the in-order traversal in a binary tree, parent pointer is available
'''

from BinaryTree import BinaryTree

def get_leftmost_child(r):
    while r.left:
        r=r.left
    return r

def get_first_right_parent(r):
    while r.parent and r.parent.left!=r:
        r=r.parent
    if not r.parent:
        return None
    else:
        return r.parent
def get_next(r):
    if r.right:
        return get_leftmost_child(r.right)
    else:
        return get_first_right_parent(r)
    
    
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
    for node in in_order:
        r=t.get_node_NR(root,node)
        print "r is ", r
        print "r's next is", get_next(r)