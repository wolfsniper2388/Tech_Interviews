''' A linked list is given such that each node contains an additional random pointer 
    which could point to any node in the list or null.
    Return a deep copy of the list.
'''

class ListNode(object):
    def __init__(self,data):
        self.data = data
        self.next = None
        self.random = None
    
    
''' Three steps:
        1. copy the node and insert the copy node between orig_node and orig_node->next
        2. copy random pointer
        3. partition the list
'''
def copy_list(orig_list):
    head = orig_list.head
    if not head:
        return None
    p = head.next
    # step 1
    while p:
        # copy the node
        copy = ListNode(p.data)
        # insert
        copy.next = p.next
        p.next = copy
        p = copy.next
    
    # step 2
    p = head.next
    while p:
        if p.random:
            copy = p.next
            copy_random = p.random.next
            # copy random pointer
            copy.random = copy_random
        # else: copy.random = None, which is default
        p = p.next.next
    
    # step 3:
    new_head = ListNode(0)
    new_head.next = head.next.next
    while p:
        # partition
        copy = p.next
        p.next = copy.next
        if copy.next:
            copy.next = copy.next.next
        # else copy.next = None, which is default
        p = p.next