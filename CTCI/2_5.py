''' Given two numbers represented by two linked lists, where each node contain a single digit. 
    Q1. The digits are stored in reverse order
    Q2. The digits are stored in forward order
    Write a function to add the two numbers and return the sum as a linked list
    Q1 E.g.
        Input: 7->1->6, 1->5->9->2 that is 617+2951
        Output: 8->6->5->3: that is 3568
'''

from LinkList import LinkList

def add_lists_reverse(list1, list2):
    ''' add two lists in reverse order
    '''
    
    head1 = list1.head
    head2 = list2.head
    p = head1.next
    q = head2.next
    carry = 0
    sum_list = LinkList()
    
    while p and q:
        curr_sum_digit = (p.data+q.data+carry) % 10
        carry = (p.data+q.data+carry) / 10
        sum_list.append_node(curr_sum_digit)
        p=p.next
        q=q.next
    while q:
        curr_sum_digit = (q.data+carry) % 10
        carry = (q.data+carry) / 10
        sum_list.append_node(curr_sum_digit)
        q=q.next
    while p:
        curr_sum_digit = (p.data+carry) % 10
        carry = (p.data+carry) / 10
        sum_list.append_node(curr_sum_digit)
        p=p.next
    if carry == 1:
        sum_list.append_node(1)
                
    return sum_list


def add_two_lists(list1, list2):
    sum_list = LinkList()
    p = list1.head.next
    q = list2.head.next
    carry = 0
    while p or q:
        first = p.data if p else 0
        second = q.data if q else 0
        sum = first+second+carry
        carry = sum/10
        sum = sum%10
        sum_list.append_node(sum)
        if p:
            p=p.next
        if q:
            q=q.next
    if carry:
        sum_list.append_node(carry)
    return sum_list

if __name__=='__main__':
    test_cases = [([7,1,6],[1,5,9,2]), ([1],[9,9,9]), ([1,2,3],[4,5,6]), ([8,5,6],[3,7,5])]
    for each_test_case in test_cases:
        list1=LinkList(each_test_case[0])
        list2=LinkList(each_test_case[1])
        print each_test_case
        add_lists_reverse(list1, list2).print_list()
        add_two_lists(list1, list2).print_list()
    