''' find the k largest elements in the BST given a root node r and k.
'''

from BinarySearchTree import BinarySearchTree



def k_largest(r, k):
    k_list = []
    stack = []
    while r or stack:
        if r:
            stack.append(r)
            r = r.right
        else:
            r=stack.pop()
            k_list.append(r)
            if len(k_list) == k:
                break
            r = r.left
    return k_list

if __name__=='__main__':
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
    
    print k_largest(r, 20)