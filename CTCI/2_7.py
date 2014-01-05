''' Check if a linked list is palindrome
'''


from LinkList import LinkList

''' push the node from start to middle to the stack
    compare the nodes from middle to the end to the top node of the stack one by one 
    until the stack is empty
 '''
def isPalindrome_1(alist):
    slow=alist.head
    fast=alist.head
    if not slow.next:
        return False
    node_stack=[]
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        node_stack.append(slow)
    if not fast:
        node_stack.pop()
    slow=slow.next
    while node_stack:
        if slow.data!=node_stack.pop().data:
            return False
        slow=slow.next
    return True



def isPalindrome_2(alist):
    return isPalindrome_2_helper(alist.head.next, len(alist))[0]


''' 3->1->2->5->2->1->3   compare 3f to 3b(return value) if equal, return (True, None)   first_node=3f, length=7
       1->2->5->2->1->3   compare 1f(3f.next) to 1b(return value) if equal, return (True, 3b(1f.next))     first_node=1f(3f.next), length=5
          2->5->2->1->3   compare 2f(1f.next) to 2b(return value) if equal, return (True, 1b(2b.next))     first_node=2f(1f.next), length=3
             5->2->1->3   first_node=5 length==1 return (True, 2b)


''' 
def isPalindrome_2_helper(first_node, length):
    if length==0:
        return (True, first_node)
    if length==1:
        return (True,first_node.next)
    front_node=first_node
    return_tuple=isPalindrome_2_helper(first_node.next,length-2)
    return_result=return_tuple[0]
    back_node=return_tuple[1]
    if return_result==False:
        return (False,back_node.next)
    if front_node.data!=back_node.data:
        return (False,back_node.next)
    else:
        return (True,back_node.next)
    
        
if __name__ == '__main__':
    a=LinkList()
    for pos,data in enumerate([3,1,2,5,2,1,3]):
        a.add_node(data,pos)
    a.print_list()
    print isPalindrome_1(a)
    print isPalindrome_2(a)