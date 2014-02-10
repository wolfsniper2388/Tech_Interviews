''' Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
    An example is the root-to-leaf path 1->2->3 which represents the number 123.
    Find the total sum of all root-to-leaf numbers.
    E.g.
        Input:
            3
           /  \
          1    2
         / \  / \
        9  7 8   2
       /
      7
        Output:
            4164(3197+317+328+322)
       
'''

from BinaryTree import BinaryTree
def sum_root_to_leaf(r):
    if not r:
        return 0
    return sum_root_to_leaf_helper(r, 0, [0])

def sum_root_to_leaf_helper(r, curr_num, sum):
    if not r:
        return 
    if not r.left and not r.right:
        sum[0]+=curr_num*10+r.data
        return sum[0]
    curr_num = curr_num *10 + r.data
    sum_root_to_leaf_helper(r.left, curr_num, sum)
    sum_root_to_leaf_helper(r.right, curr_num, sum)
    return sum[0]

if __name__=='__main__':
    t=BinaryTree()
    pre_order=[3,1,9,7,7,2,8,2]
    in_order=[7,9,1,7,3,8,2,2]
    t.create_tree(pre_order, in_order)
    
    
    print sum_root_to_leaf(t.root)
    
    