''' Give a binary tree. Create a linked list of all the nodes at each depth
'''

from BinaryTree import BinaryTree
from LinkList import LinkList
from collections import deque

# level order traversal
def create_lists_1(r):
    q=deque([])
    level=deque([])
    lists=[]
    q.append(r)
    level.append(0)
    level_list=LinkList()
    level_list.append_node(r)

    while q:
        current_node=q.popleft()
        current_level=level.popleft()
        if current_node.left:
            q.append(current_node.left)
            level.append(current_level+1)
        if current_node.right:
            q.append(current_node.right)
            level.append(current_level+1)
        
        if q:
            # if this node is at the same level of the previous node, then add this node to the list
            if level[0]==current_level:
                level_list.append_node(q[0])
            # else, then pack the list to lists, create a new list, and add this node to the list
            else:
                lists.append(level_list)
                level_list=LinkList()
                level_list.append_node(q[0])
        # if it's the last element, pack to lists
        else:
            lists.append(level_list)
    return lists


# modification of bfs
def create_lists_2(r):
    lists=[]
    current=LinkList()
    if r:
        current.append_node(r)
    while len(current)>0:
        lists.append(current)       # pack to lists
        parents=current     # go one level down
        current=LinkList()  # create a new list
        for parent in parents:
            if parent.left:
                current.append_node(parent.left)
            if parent.right:
                current.append_node(parent.right)
    return lists
  
  
     
def create_lists_3(r):
    result_lists=[]
    # python list is mutable, so the result_lists will change after the call
    create_lists_3_helper(r, result_lists, 0)
    return result_lists

# modification of pre-order traversal
def create_lists_3_helper(r, lists, level):
    if not r:
        return
    # if the level is not visited before, create a new list
    if level>len(lists)-1:
        current_list=LinkList()
        current_list.append_node(r)
        lists.append(current_list)
    # else, get the list, append the tree node
    else:
        current_list=lists[level]
        current_list.append_node(r)
        
    create_lists_3_helper(r.left, lists, level+1)
    create_lists_3_helper(r.right, lists, level+1)
 

        
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
    t=BinaryTree();
    pre_order=[1,2,4,5,6,12,7,3,8,9,10,11]
    in_order=[4,2,12,6,5,7,1,8,3,10,9,11]
    root=t.create_tree(pre_order, in_order)
    print 'Testing create_lists_1'
    lists=create_lists_1(root)
    for each_list in lists:
        each_list.print_list()
        print
        
    print 'Testing create_lists_2'
    lists=create_lists_2(root)
    for each_list in lists:
        each_list.print_list()
        print
        
    print 'Testing create_lists_3'
    lists=create_lists_3(root)
    for each_list in lists:
        each_list.print_list()
        print