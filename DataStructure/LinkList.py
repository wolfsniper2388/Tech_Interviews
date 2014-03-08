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
        self.head=ListNode(0)
        if seq:
            for data in seq:
                self.append_node(data)
    
    def __repr__(self):
        return '%s(%r)' %(self.__class__.__name__, self.head)
    
    def __len__(self):
        p=self.head.next
        length=0
        while p:
            length+=1
            p=p.next
        return length
    
    def __iter__(self):
        p=self.head.next
        it=[]
        while p!=None:
            it.append(p.data)
            p=p.next
        return iter(it)
    
    def add_node(self,data,pos):
        '''add node at the position pos starting from 0
        e.g 
        pos: 0 1 2 3 4 5
        list: 2 7 9 8 3
        '''
        if pos>len(self):
            print 'Wrong position'        
            return 
        p=ListNode(data)
        q=self.head
        for i in range(pos):
            q=q.next
        p.next=q.next
        q.next=p
        
    def append_node(self,data):
        self.add_node(data, len(self))
    
    def get_tail_node(self):
        p = self.head
        if not p.next:
            return None
        while p.next:
            p = p.next
        return p
        
    def del_node_value(self,data):
        'delete the node by its value'
        p=self.head
        while p.next and p.next.data!=data:
            p=p.next
        if p.next==None:
            print data,'Not found in the list'
            return
        q=p.next
        p.next=q.next
        del q
    
    def del_node_pos(self,pos):
        ''' delete ListNode at the position starting from 0
            e.g.
            pos:  0 1 2 3 4
            list: 2 7 9 8 3
        '''
        if pos>len(self)-1:
            raise IndexError(pos)
        p=self.head
        for i in range(pos):
            p=p.next
        q=p.next
        p.next=q.next
        del q
   
    def print_list(self):
        current=self.head.next
        while current:
            print current.data,
            current=current.next
        print
        
    def reverse_list(self):
        p=self.head.next
        if p==None or p.next==None:
            return
        self.head.next=None
        while p:
            q=p.next    #record p's next
            p.next=self.head.next   #the following two steps is equivalent to inserting p at position 0
            self.head.next=p
            #self.add_node(p.data, 0)
            p=q
    
    def make_loop(self,pos):
        'Make the linked list a loop between pos and tail, pos starts from 0'
        if pos>len(self)-1:
            print 'Wrong position'        
            return 
        tail=self.head.next
        while tail.next:
            tail=tail.next
        p=self.head.next
        for i in range(pos):
            p=p.next
        tail.next=p
        
    def get_loop_point(self):
        'Get the interjection of the loop point, i.e. the parameter pos of make_loop'
        p=self.head.next.next
        q=self.head.next
        while p!=q:
            p=p.next.next
            q=q.next
        q=self.head
        while p!=q:
            p=p.next
            q=q.next
        return p
    
    def loop_length(self):
        p=self.get_loop_point()
        loopDict={}
        length=0   
        while p not in loopDict:
            loopDict[p]=1
            length+=1
            p=p.next
        return length
        
if __name__ == '__main__':
    b=LinkList([1,2,3])
    b.print_list()
    a=LinkList()
    a.append_node(3)
    a.print_list()
    data=[5,8,9,10,3]
    for each_data in data:
        a.append_node(each_data)
    print 'Test creating list'
    a.print_list()
    print 'List length is ', len(a)
    
    print 'Test adding node'
    a.add_node(6,3)
    a.print_list()
    print 'List length is ', len(a)
    
    print 'Test deleting node by value'
    a.del_node_value(2)
    a.print_list()
    print 'List length is ', len(a)
    
    print 'Test deleting node by position'
    a.del_node_pos(0)
    a.print_list()
    print 'List length is ', len(a)
    
    print 'Test iterating'
    for d in a:
        print d
    
    print 'Test reverse'
    a.reverse_list()
    a.print_list()
    
    print 'Test loop'
    a.make_loop(1)
    print 'loop point is', a.get_loop_point().data
    print 'loop length is', a.loop_length()