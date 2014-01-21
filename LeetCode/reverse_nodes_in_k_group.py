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
from LinkList import LinkList

def need_reverse(new_head,k):
    new_head = new_head.next
    while new_head:
        new_head=new_head.next
        k-=1
        if k==0:
            return True
    return False
'''
def reverse(new_head,k):
    k-=1
    p=new_head.next
    while k > 0:
        q=p.next
        p.next=q.next
        q.next=new_head.next
        new_head.next=q
        k-=1
''' 
def reverse_nodes_in_k_group(my_list, k):
    new_head = my_list.head
    orig_k=k
    while need_reverse(new_head, orig_k):
        k = orig_k-1
        p=new_head.next
        while k > 0:
            q=p.next
            p.next=q.next
            q.next=new_head.next
            new_head.next=q
            k-=1
        new_head = p
    return my_list
    
if __name__=='__main__':
    test_cases=[([1,2,3,4,5],2), ([1,2,3,4,5],3)]
    for each_test_case in test_cases:
        linkedlist = LinkList(each_test_case[0])
        k = each_test_case[1]
        reverse_nodes_in_k_group(linkedlist, k).print_list()
