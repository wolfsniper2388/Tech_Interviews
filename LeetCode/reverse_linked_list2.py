''' Reverse a linked list from position m to n. Do it in-place and in one-pass.
    E.g
    Input: 1->2->3->4->5->NULL, m = 2 and n = 4,
    Output: 1->4->3->2->5->NULL.
    Note:
    Given m, n satisfy the following condition:
    1 <= m <= n <= length of list.
'''

from LinkList import *

def reverse_linked_list(orig_list, m, n):
    assert(1 <= m <= n <= len(orig_list))
    dummy = ListNode(0)
    dummy.next = orig_list.head
    p = dummy
    count = n-m
    while m-1 > 0:
        p = p.next
        m-=1
    q = p.next    
    while count > 0:
        r = q.next
        q.next = r.next
        r.next = p.next
        p.next = r
        count -= 1
    orig_list.head = dummy.next
    return orig_list

if __name__=='__main__':
    test_cases = [([1,2,3,4,5,6],6,6), ([1,2,3],1,3)]
    for each_test_case in test_cases:
        orig_list_data, m, n= each_test_case
        orig_linkedlist = LinkList(orig_list_data)
        print each_test_case
        reverse_linked_list(orig_linkedlist, m,n).print_list() 