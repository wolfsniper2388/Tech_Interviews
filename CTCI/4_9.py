''' Given a binary tree where each node contains a number value, Print all paths which sum to a given ValueError
    The path does not need to start at the root or end at a leaf
'''


from BinaryTree import BinaryTree

def find_path(r,n,path):
    if not r:
        return 
    val_sum=0
    path.insert(0,r.data)
    for pos,value in enumerate(path):
        val_sum+=value
        if val_sum==n:
            print path[:pos+1]
    find_path(r.left, n, path)
    find_path(r.right, n, path)
    path.pop(0)

if __name__=='__main__':
    ''' The tree is:
                     1
                   /   \ 
                 2      3
                / \    / \
               5   4  8   9
                  / \    / \
                 6   7  10  11
                /
               12
    '''
    t=BinaryTree();
    pre_order=[1,2,5,4,6,12,7,3,8,9,10,11]
    in_order=[5,2,12,6,4,7,1,8,3,10,9,11]
    root=t.create_tree(pre_order, in_order)
    
    
    find_path(root, 12, [])