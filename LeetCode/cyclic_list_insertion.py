''' Given a node from a cyclic linked list which has been sorted, 
    write a function to insert a value into the list 
    such that it remains a cyclic sorted list. 
    The given node can be any single node in the list.
    E.g. 
                       ________
                      /        \
        Input: list: 1->3->3->4, Given node: 3, 
                node-to-insert : 2, 3, 5
                
        Output: 
                  __________
                 /          \
                1->2->3->3->4
                 ___________
                /           \
                1->3->3->3->4
                  __________
                 /          \
                1->3->3->4->5
    You can assume the passed in linklist is always not None
'''

from LinkList import *

def insert_node_cyclic(orig_list, node, val):
    p = node
    prev = None
    while True:
        prev = p
        p = p.next
        # case 1: insert between previous and current
        if prev.data <= val <= p.data:
            break
        # case 2: insert at end or beginning
        if prev.data > p.data and (val > prev.data or val < p.data):
            break
        # case 3: when duplicates in list, traverse back to start point
        if p == node:
            break
    new_node = ListNode(val)
    prev.next = new_node
    new_node.next = p
    #return orig_list
    
if __name__=='__main__':
    orig_list = LinkList([1,3,3,4])
    p = q = orig_list.head
    orig_list.make_loop(0)
    node = q.next.next      # node = second 3
    print orig_list.loop_length()
    for val in [2,3,5]:
        insert_node_cyclic(orig_list, node, val)
        p = q = orig_list.head
        print p.data,
        p = p.next
        while p!=q:
            print p.data,
            p = p.next
        print