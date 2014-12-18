''' Given a linked list, swap every two adjacent nodes and return its head.
    E.g
        Input: 1->2->3->4
        Output: 2->1->4->3
        Input: 1->2->3
        Output: 2->1->3
    Your algorithm should use only constant space. 
    You may not modify the values in the list, only nodes itself can be changed.
'''
from LinkList import *

def swap_nodes(my_list):
    dummy = ListNode(0)
    dummy.next = my_list.head
    p = dummy
    while p.next and p.next.next:
        q=p.next
        r=q.next
        if not r:
            return my_list
        p.next=r
        q.next=r.next
        r.next=q
        p=q
    my_list.head = dummy.next
    return my_list

if __name__=='__main__':
    test_cases=[[1,2,3,4,5,6], [1,2,3,4,5], [1,2,3,4], [1,2,3], [1,2], [1], []]
    for each_test_case in test_cases:
        curr_linkedlist = LinkList(each_test_case)
        swap_nodes(curr_linkedlist).print_list()