''' Q1.
    Sort a linked list using insertion sort.
    Q2.
    Sort a linked list using merge sort
'''
from LinkList import *
def insertion_sort_list(orig_list):
    dummy = ListNode(0)
    dummy.next = orig_list.head
    if not orig_list.head:
        return
    q = orig_list.head.next
    q_pre = orig_list.head
    
    while q:
        p = dummy
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
    orig_list.head = dummy.next
    return orig_list

def merge_sort_list(orig_list):
    nh = merge_sort_list_helper(orig_list.head)
    result_list = LinkList()
    result_list.head = nh
    return result_list

def merge_sort_list_helper(head):
    if not head or not head.next:
        return head
    dummy = ListNode(0)
    dummy.next = head
    slow = dummy
    fast = dummy
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    l1 = head
    l2 = slow.next
    slow.next = None
    nh_1 = merge_sort_list_helper(l1)
    nh_2 = merge_sort_list_helper(l2)
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
        
if __name__=='__main__':
    test_cases = [[3,7,4,8,6,5],[10,7,4,11,5,2,6,19,1],[1],[5,4],[6,5,4,3,2,2],[10,4,7,11,5,11,2,4]]
    for each_test_case in test_cases:
        orig_list = LinkList(each_test_case)
        insertion_sort_list(orig_list).print_list()
        orig_list = LinkList(each_test_case)
        merge_sort_list(orig_list).print_list()
        
        