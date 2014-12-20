''' Remove Duplicates from sorted array
    Q1. Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
    Do not allocate extra space for another array, you must do this in place with constant memory.
    E.g.
        Input: [1,1,2]
        Output: [1,2]
    
    Q2. What if duplicates are allowed at most twice?
    E.g.
        Input: [1,1,1,2,2,3]
        Output: [1,1,2,2,3]
        
    Remove Duplicates from sorted linked list
    Q1. Given a sorted linked list, delete all duplicates such that each element appear only once.
    E.g.
        Input: 1->2->2->2->3->3
        Output: 1->2->3
    Q2. Given a sorted linked list, delete all nodes that have duplicate numbers, 
        leaving only distinct numbers from the original list.
    E.g.    
        Input: 1->2->3->3->4->4->5
        Output: 1->2->5
        Input: 1->1->1->2->3
        Ouptu: 2->3
    
    Remove element
    Given an array and a value, remove all instances of that value in place and return the new length.
    The order of elements can be changed. It doesn't matter what you leave beyond the new length.
'''

def remove_dup_in_array_q1(A):
    ''' remove duplicates in an array so that each element only occur once
    '''
    # i: new index, j: original index in A
    i=0
    for j in range(1, len(A)):
        if A[i] != A[j]:
            A[i+1]=A[j]
            i+=1
    return A[:i+1]

def remove_dup_in_array_q2(A):
    ''' for numbers that are duplicated for 3 times or more, reduce the duplicates to 2
        for others, remain same
    '''
    if len(A) <= 2:
        return A
    # i: new index, j: original index in A
    i=1
    for j in range(2, len(A)):
        # if A[j]==A[i]==A[i-1], j moves forward, if not, copy A[j] to A[i+1], i moves forward
        if not (A[j]==A[i] and A[j]==A[i-1]):
            A[i+1]=A[j]
            i+=1
    return A[:i+1]


from LinkList import *

def remove_dup_in_list_q1(my_list):
    ''' remove duplicates in linked list so that each element occur only once 
    '''
    p = my_list.head
    q = p.next
    while q:
        if p.data == q.data:
            p.next = q.next
            del q
            q = p.next
        else:
            p = q
            q = q.next
    return my_list

def remove_dup_in_list_q2(my_list):
    ''' remove all nodes with duplicates, leaving only distinctive elements
    '''
    if not my_list.head:
        return None
    dummy = ListNode(0)
    dummy.next = my_list.head
    p = dummy
    q = p.next.next
    del_flag = False
    while q:
        if q.data!=p.next.data:
            if not del_flag:
                p=p.next
                q=q.next
            else:
                p.next=q
                q=q.next
                del_flag=False
        else:
            q=q.next
            del_flag=True
        
    # deal with situations like 1->1, 1->2->2->3->3
    if del_flag:
        p.next = None
    return my_list

''' Given an array and a value, remove all instances of that value in place and return the new array.
    The order of elements can be changed. It doesn't matter what you leave beyond the new length.
'''
def remove_elem(A, elem):
    i=0
    for j in range(len(A)):
        if A[j]!=elem:
            A[i]=A[j]
            i+=1
    return A[:i]

if __name__=='__main__':
    test_cases = [[1,1,2], [1,1,2,3,3,3,4,4], [1,2,3], [1]]
    for each_test_case in test_cases:
        print 'remove dup in array, Q1',each_test_case, remove_dup_in_array_q1(each_test_case)
    test_cases = [[1,1,2], [1,1,2,3,3,3,4,4], [1,2,3], [1], [1,2,2,2,3,3,4,4,4], [1,2,2,2,3,3,4,4,4,4,5,6]]
    for each_test_case in test_cases:
        print 'remove dup in array Q2',each_test_case, remove_dup_in_array_q2(each_test_case)
    
    test_cases = [[1,2,2,2,3,3], [1], [1,1,1,1],[1,2,2,2,3,3,4]]
    for each_test_case in test_cases:
        print 'remove dup in list Q1',each_test_case
        remove_dup_in_list_q1(LinkList(each_test_case)).print_list()
    test_cases = [[1,1],[1,1,1,2,3],[1], [1,2,2,2,3,3,3]]
    for each_test_case in test_cases:
        print 'remove dup in list Q2',each_test_case
        remove_dup_in_list_q2(LinkList(each_test_case)).print_list()
    
    for each_test_case in test_cases:
        print 'remove element in array', each_test_case, remove_elem(each_test_case, 1)