''' Merge two sorted linked lists and return it as a new list. 
    The new list should be made by splicing together the nodes of the first two lists.

'''

from LinkList import LinkList

def merge_two_lists(listA, listB):
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

if __name__=='__main__':
    test_cases = [([1,3,5,6],[2,4]), ([1,3,5],[]), ([1,2,3,4],[5,6,7,8])]
    for each_test_case in test_cases:
        listA_list,listB_list=each_test_case
        listA = LinkList(listA_list)
        listB = LinkList(listB_list)
        merge_two_lists(listA, listB).print_list()