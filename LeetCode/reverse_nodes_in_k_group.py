''' Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
    If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
    You may not alter the values in the nodes, only nodes itself may be changed.
    Only constant memory is allowed.
    E.g
        Input: 1->2->3->4->5, k=2
        Output: 2->1-4->3->5
        Input: 1->2->3->4->5, k=3
        Output: 3->2->1->4->5
'''
from LinkList import *

def reverse_nodes_in_k_group(my_list, k):
    i=0
    dummy = ListNode(0)
    dummy.next = my_list.head
    h = my_list.head
    new_head = dummy
    while h:
        i+=1
        if i % k == 0:
            new_head = reverse(new_head, k)
            h = new_head.next
        else:
            h = h.next
    my_list.head = dummy.next
    return my_list

def reverse(new_head, k):
    p = new_head.next
    while k-1 > 0:
        q=p.next
        p.next=q.next
        q.next=new_head.next
        new_head.next=q
        k-=1
    return p
    
if __name__=='__main__':
    test_cases=[([1,2,3,4,5],2), ([1,2,3,4,5],3)]
    for each_test_case in test_cases:
        linkedlist = LinkList(each_test_case[0])
        k = each_test_case[1]
        reverse_nodes_in_k_group(linkedlist, k).print_list()
