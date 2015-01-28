'''
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 -> a2
                    \
                     c1 -> c2 -> c3
                    /          
B:     b1 -> b2 -> b3
begin to intersect at node c1.
'''
from LinkList import *

def get_intersection_node(listA, listB):
    headA = listA.head
    headB = listB.head
    if not headA or not headB:
        return None
    tailA = headA
    tailB = headB
    lenA = lenB = 0
    while tailA.next:
        tailA = tailA.next
        lenA += 1
    while tailB.next:
        tailB = tailB.next
        lenB += 1
    if tailA is not tailB:
        return None
    if lenA < lenB:
        diff = lenB-lenA
        while diff > 0:
            headB = headB.next
            diff -= 1
    elif lenB < lenA:
        diff = lenA-lenB
        while diff > 0:
            headA = headA.next
            diff -= 1
    while headA:
        if headA == headB:
            return headA
        headA = headA.next
        headB = headB.next
        
        
if __name__=='__main__':
    la = LinkList([1,3,5,6,7,8,9,10])
    lb = LinkList([2,4])
    tb = lb.get_tail_node()
    tb.next = la.head.next.next.next
    lb.print_list()
    
    print get_intersection_node(la, lb)