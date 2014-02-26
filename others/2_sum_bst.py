''' find two nodes in a binary search tree such that their values sum up to a given number: target
    It's guaranteed that only one pair exists
    E.g.
        Input: 
                10
               / \
              5   16
             / \
            2   8
            
        target = 13
        Output:(5,8)
'''

from BinarySearchTree import BinarySearchTree

def normal_next(curr_node, normal_stack):
    'return the next node of curr_node in the in-order traversal'
    if normal_stack:
        normal_stack.pop()
    if curr_node.right:
        next_node = curr_node.right
        while next_node:
            normal_stack.append(next_node)
            next_node = next_node.left
    return normal_stack[-1]

    
    
def reverse_next(curr_node, reverse_stack):
    'return the next node of curr_node in the reverse-in-order traversal'
    if reverse_stack:
        reverse_stack.pop()
    if curr_node.left:
        next_node = curr_node.left
        while next_node:
            reverse_stack.append(next_node)
            next_node = next_node.right
    return reverse_stack[-1]

    
def two_sum_bst(root, target):
    normal_stack=[]
    reverse_stack=[]
    start=root
    end=root
    while start:
        normal_stack.append(start)
        start=start.left
    start = normal_stack[-1]
    while end:
        reverse_stack.append(end)
        end=end.right
    end = reverse_stack[-1]
    while start.data<end.data:
        if start.data+end.data < target:
            start = normal_next(start, normal_stack)
        elif start.data+end.data > target:
            end = reverse_next(end, reverse_stack)
        else:
            return (start.data, end.data)
    return None

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
    test_cases = [91, 60, 11,108,57,24,200]
    for each_test_case in test_cases:
        print two_sum_bst(r, each_test_case)