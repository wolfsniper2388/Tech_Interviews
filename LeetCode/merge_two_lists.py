''' Merge two sorted linked lists and return it as a new list. 
    The new list should be made by splicing together the nodes of the first two lists.

'''

from LinkList import LinkList

# iterative
def merge_two_lists_1(listA, listB):
    p = listA.head.next
    q = listB.head.next
    if not p:
        return listB
    if not q:
        return listA 
    result_list = LinkList()
    r = result_list.head
    while p and q:
        if p.data < q.data:
            result_list.append_node(p.data)
            p = p.next
        else:
            result_list.append_node(q.data)
            q = q.next
        r = r.next
    if p:
        r.next = p
    if q:
        r.next = q
    return result_list

# recursive
def merge_two_lists_2(list_1, list_2):
    result = LinkList()
    result.head.next = merge_two_lists_helper(list_1.head.next, list_2.head.next)
    return result
    
def merge_two_lists_helper(head_1, head_2):
    if not head_1:
        return head_2
    if not head_2:
        return head_1
    if head_1.data < head_2.data:
        ret = head_1
        ret.next = merge_two_lists_helper(head_1.next, head_2)
    else:
        ret = head_2
        ret.next = merge_two_lists_helper(head_1, head_2.next)
    return ret
    
if __name__=='__main__':
    test_cases = [([1,3,5,6],[2,4]), ([1,3,5],[]), ([1,2,3,4],[5,6,7,8])]
    for each_test_case in test_cases:
        listA_list,listB_list=each_test_case
        listA = LinkList(listA_list)
        listB = LinkList(listB_list)
        merge_two_lists_1(listA, listB).print_list()
        merge_two_lists_2(listA, listB).print_list()