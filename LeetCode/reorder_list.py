''' Given a singly linked list L: L0->L1->...->Ln-1->Ln,
    reorder it to: L0->Ln->L1->Ln-1->L2->Ln-2->...
    You must do this in-place without altering the nodes' values.
    E.g.
        Input: 3->5->7->4->2->6->1
        OuputL 3->1->5->6->7->2->4
'''

from LinkList import LinkList

def reorder_list(orig_list):
    p=q=orig_list.head
    # find the break point
    while p and p.next:
        p = p.next.next
        q = q.next
    
    # break the list
    r = q.next
    q.next = None
    second_half = LinkList()
    second_half.head.next = r
    
    # reverse the second half
    second_half.reverse_list()
    
    # merge
    p = orig_list.head.next
    r = second_half.head.next
    while r:
        p_next = p.next
        r_next = r.next
        r.next = p.next
        p.next = r
        r = r_next
        p = p_next
    del second_half
    return orig_list

if __name__=='__main__':
    test_cases = [[3,5,7,4,2,6,1],[3,5,7,4,2,6,1,10]]
    for each_test_case in test_cases:
        orig_list = LinkList(each_test_case)
        reorder_list(orig_list).print_list()