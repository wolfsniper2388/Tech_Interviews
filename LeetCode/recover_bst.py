''' Two elements of a binary search tree (BST) are swapped by mistake.
    Recover the tree without changing its structure using O(1) space
'''
from BinarySearchTree import *

prev = first = second = None

''' first: first swapped node
    second: second swapped node
    prev: previous node in in-order traversal
    r: current node
'''
def recover_bst_in_order(r):
    global prev, first, second
    if r:
        recover_bst_in_order(r.left)
        if not prev:
            prev = r
        else:
            if r.data < prev.data:
                if not first:
                    first = prev
                # if first is second's direct prior in in-order traversal, second is r
                # otherwise second will be overwritten later
                second = r
            prev = r    
        recover_bst_in_order(r.right)

def recover_bst(r):
    recover_bst_in_order(r)
    print first,second
    first.data, second.data = second.data, first.data
    return r

if __name__=='__main__':
    t=BinarySearchTree()
    data = [1,2,6,4,5,3,7,8]
    t.create_tree(data)    
    recover_bst(t.root)
    t.in_order_print(t.root)
