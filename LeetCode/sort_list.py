''' Q1.
    Sort a linked list using insertion sort.
    Q2.
    Sort a linked list using merge sort
'''
from LinkList import *
def insertion_sort_list(orig_list):
    head = orig_list.head
    if not head.next:
        return
    q=head.next.next
    q_pre = head.next
    while q:
        p = head
        # find the position to insert q
        while q.data > p.next.data:
            p = p.next
        if p.next == q:
            q_pre = q
            q = q.next
        else:
            # insert q between p and p_next
            p_next = p.next
            q_pre.next = q.next
            p.next = q
            q.next = p_next
            q = q_pre.next
    return orig_list

def merge_sort_list_1(head):
    if not head or not head.next:
        return head
    dummy = ListNode(0)
    dummy.next= head
    slow = dummy
    fast = dummy
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    l1 = head
    l2 = slow.next
    slow.next = None
    nh_1 = sortList(l1)
    nh_2 = sortList(l2)
    return merge(nh_1, nh_2)
    
def merge(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    if l1.data <= l2.data:
        l1.next = merge(l1.next, l2)
        return l1
    else:
        l2.next = merge(l1, l2.next)
        return l2


def merge_sort_list_2(orig_list):
    # no element in list
    if not orig_list.head.next:
        return 
    # only one element in list
    if not orig_list.head.next.next:
        return orig_list
    
    # get the middle
    fast=slow=orig_list.head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        
    # break the list
    q=slow.next
    slow.next = None
    second_half=LinkList()
    second_half.head.next = q
    
    # sort first and second halves
    first_half_sorted = merge_sort_list(orig_list)
    second_half_sorted = merge_sort_list(second_half)
    
    # merge
    p = first_half_sorted.head.next
    q = second_half_sorted.head.next

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
    test_cases = [[3,7,4,8,6,5],[10,7,4,11,5,2,6,19,1],[1],[5,4],[6,5,4,3,2,2],[10,4,7,11,5,11,2,4], []]
    for each_test_case in test_cases:
        orig_list = LinkList(each_test_case)
        h = sortList(orig_list.head.next)
        while h:
            print h.data,
            h = h.next
        print
        #insertion_sort_list(orig_list).print_list()
        #orig_list = LinkList(each_test_case)
        #merge_sort_list(orig_list).print_list()
        