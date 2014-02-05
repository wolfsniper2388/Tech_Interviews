''' Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
'''

from LinkList import *
from BinaryTree import *

curr_node = None
def list2bst(my_list):
    global curr_node
    curr_node = my_list.head.next
    root = list2bst_helper(0, len(my_list)-1)
    return BinaryTree(root)


def list2bst_helper(start, end):
    global curr_node
    if start > end:
        return None
    mid = start+(end-start)/2
    left_child = list2bst_helper(start, mid-1)
    parent = TreeNode(curr_node.data)
    curr_node = curr_node.next
    parent.left = left_child
    parent.right = list2bst_helper(mid+1, end)
    return parent


if __name__=='__main__':
    test_cases = [[1,2,3,4,5,6]]
    for each_test_case in test_cases:
        my_list = LinkList(each_test_case)
        bst = list2bst(my_list)
        bst.pre_order_print(bst.root)
        print
        bst.in_order_print(bst.root)