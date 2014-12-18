''' Merge two sorted linked lists and return it as a new list. 
    The new list should be made by splicing together the nodes of the first two lists.

'''

from LinkList import *

# iterative
def merge_two_lists_1(listA, listB):
    p = listA.head
    q = listB.head
    if not p:
        return listB
    if not q:
        return listA 
    result_list = LinkList()
    #tail = ListNode(0)
    #tail.next = result_list.head
    while p and q:
        if p.data < q.data:
            result_list.append_node(ListNode(p.data))
            p = p.next
        else:
            result_list.append_node(ListNode(q.data))
            q = q.next
        
    if p:
        result_list.append_node(p)
    if q:
        result_list.append_node(q)
    return result_list

# recursive
def merge_two_lists_2(list_1, list_2):
    result = LinkList()
    result.head = merge_two_lists_helper(list_1.head, list_2.head)
    return result
    
def merge_two_lists_helper(head_1, head_2):
    if not head_1:
        return head_2
    if not head_2:
        return head_1
    if head_1.data < head_2.data:
        head_1.next = merge_two_lists_helper(head_1.next, head_2)
        return head_1
    else:
        head_2.next = merge_two_lists_helper(head_1, head_2.next)
        return head_2
    
if __name__=='__main__':
    test_cases = [([1,3,5,6],[2,4]), ([1,3,5],[]), ([1,2,3,4],[5,6,7,8]),([2],[1])]
    for each_test_case in test_cases:
        listA_list,listB_list=each_test_case
        listA = LinkList(listA_list)
        listB = LinkList(listB_list)
        merge_two_lists_1(listA, listB).print_list()
        merge_two_lists_2(listA, listB).print_list()