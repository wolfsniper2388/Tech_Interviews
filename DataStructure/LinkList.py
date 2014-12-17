''' Implement a linked list
'''

class ListNode(object):
    'LinkList ListNode'
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return '%s(%r)' %(self.__class__.__name__, self.data)

class LinkList(object):
    'A Linked list class that supports operation of adding, deleting ListNodes'
    def __init__(self, seq=None):
        self.head = None
        if seq:
            for data in seq:
                self.append_node(ListNode(data))
    
    def __repr__(self):
        return '%s(%r)' %(self.__class__.__name__, self.head)
    
    def __len__(self):
        p = self.head
        length = 0
        while p:
            length += 1
            p = p.next
        return length
    
    def __iter__(self):
        p=self.head
        it=[]
        while p:
            it.append(p.data)
            p = p.next
        return iter(it)
    
    def add_node(self,node,pos):
        '''add node at the position pos starting from 0
        e.g 
        pos: 0 1 2 3 4 5
        list: 2 7 9 8 3
        return  0 if success
                1 if failed
        '''
        dummy = ListNode(0)
        dummy.next = self.head
        p = dummy
        for i in range(pos):
            p = p.next
            if not p:
                print 'Wrong position'
                return 1
        
        node.next = p.next
        p.next = node
        return 0
        
    def append_node(self, node):
        p = self.get_tail_node()
        if not p:
            self.head = node
            return
        p.next = node
        
    def get_tail_node(self):
        p = self.head
        if not p:
            return None
        while p.next:
            p = p.next
        return p
        
    def del_node_by_value(self,data):
        'delete all nodes with the certain @p data'
        if not self.head:
            return
        dummy = ListNode(0)
        dummy.next = self.head
        
        prev = dummy
        curr = self.head
        
        while curr:
            if curr.data == data:
                prev.next = curr.next
                del curr
                curr = prev.next
            else:
                prev = curr
                curr = curr.next
    
    def del_node_by_pos(self, pos):
        ''' delete ListNode at the position starting from 0
            e.g.
            pos:  0 1 2 3 4
            list: 2 7 9 8 3
            return  0 if success
                    1 if failed
        '''
        if not self.head:
            return 1
        if pos == 0:
            self.head = self.head.next
            return 0
        dummy = ListNode(0)
        dummy.next = self.head
        p = dummy
        for i in range(pos):
            p = p.next
            if not p.next:
                print 'pos out of range'
                return 1
        q = p.next
        p.next = q.next
        del q
        return 0
   
    def print_list(self):
        curr = self.head
        while curr:
            print curr.data,
            curr = curr.next
        print
        
    def reverse_list(self):
        dummy = ListNode(0)
        p = self.head
        if not p or not p.next:
            return
        while p:
            q = p.next    #record p's next
            p.next = dummy.next   #the following two steps is equivalent to inserting p at position 0
            dummy.next=p
            #self.add_node(p.data, 0)
            p = q
        self.head = dummy.next
    
    def reverse_list_recur(self):
        if not self.head or not self.head.next:
            return
        self.reverse_list_recur_helper(self.head)
        
    def reverse_list_recur_helper(self, p):
        if not p.next:
            return p
        new_head = self.reverse_list_recur_helper(p.next)
        p.next.next = p
        p.next = None
        self.head = new_head
        return new_head
    
    
    def make_loop(self, pos):
        'Make the linked list a loop between pos and tail, pos starts from 0'
        if pos>len(self)-1:
            print 'Wrong position'        
            return 
        tail = self.get_tail_node()
        p = self.head
        for i in range(pos):
            p = p.next
        tail.next = p
        
    def get_loop_point(self):
        'Get the loop start point, i.e. the parameter pos of make_loop'
        if not self.head:
            return None
        dummy = ListNode(0)
        dummy.next = self.head
        p = self.head.next
        q = self.head
        while p != q:
            p = p.next.next
            q = q.next
        q = dummy
        while p != q:
            p = p.next
            q = q.next
        return p
    
    def loop_length(self):
        p = self.get_loop_point()
        if not p:
            return -1
        q = p.next
        loop_len = 1
        while q != p:
            q = q.next
            loop_len += 1
        return loop_len
        
if __name__ == '__main__':
    b=LinkList([1,2,3])
    b.print_list()
    a=LinkList()
    a.append_node(ListNode(3))
    a.print_list()
    data=[5,5,8,5,5,5,9,10,3,5,5]
    for each_data in data:
        a.append_node(ListNode(each_data))
    print 'Test creating list'
    a.print_list()
    print 'List length is ', len(a)
    
    print 'Test adding node'
    a.add_node(ListNode(6), 3)
    a.print_list()
    print 'List length is ', len(a)
    
    print 'Test deleting node by value, deleting 5'
    a.del_node_by_value(5)
    a.print_list()
    print 'List length is ', len(a)
    
    print 'Test deleting node by position'
    a.del_node_by_pos(0)
    a.print_list()
    print 'List length is ', len(a)
    
    print 'Test iterating'
    for d in a:
        print d,
    print
    
    print 'Test reverse'
    a.print_list()
    a.reverse_list()
    a.print_list()
    a.reverse_list_recur()
    a.print_list()
    
    print 'Test loop'
    a.make_loop(1)
    print 'loop point is', a.get_loop_point().data
    print 'loop length is', a.loop_length()
    
    l1 = LinkList()
    #l1.append_node(ListNode(1))
    l1.print_list()
    #l1.head.next = l1.head
    print l1.get_loop_point()
    print l1.loop_length()