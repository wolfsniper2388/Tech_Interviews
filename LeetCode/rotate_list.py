''' Given a list, rotate the list to the right by k places, where k is non-negative and less than the length of the list
    E.g.
    Input: 1->2->3->4->5->NULL, k = 2,
    Output: 4->5->1->2->3->NULL.
'''
from LinkList import *

def rotate_list(orig_list, k):
    if k==0:
        return orig_list
    p = q = orig_list.head
    # i = 0,1,...k-1
    for i in range(k):
        p = p.next
        if not p:
            return None
    
    while p.next:
        q=q.next
        p=p.next
    ''' till now, p points to the last element in list
        and q points to the last k+1 element
    '''
    p.next = orig_list.head
    orig_list.head = q.next
    q.next = None
    return orig_list

if __name__=='__main__':
    test_cases = [([1,2,3,4], 2), ([1,2],1), ([1,2,3,4,5],3), ([1,2,3,4,5], 4)]
    for each_test_case in test_cases:
        orig_list = LinkList(each_test_case[0])
        k = each_test_case[1]
        print orig_list, k
        rotate_list(orig_list,k).print_list()