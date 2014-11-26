''' Implement a id allocation class, the class allocates an id when caller requests an id, and recycle an id when caller returns it back
    Assume the id ranges from 1 to n
'''

class FreeList(object):
    def __init__(self, size):
        self.size = size    # id ranges from 1 to size
        self.fl = [0]*(size+1)
        self.count = size
        for i in range(1,size):
            self.fl[i] = i+1
        self.fl[size] = 0
        self.head_id = 1
        self.tail_id = size
        
    def alloc(self):
        if self.count == 0:
            assert(self.head_id==0 and self.tail_id == 0)
            print 'cannot allocate'
            return
        id = self.head_id
        self.head_id = self.fl[self.head_id]
        if self.head_id == 0:
            self.tail_id = 0
        self.fl[id] = -1
        self.count-=1
        return id
 
    
    def recycle(self, id):
        assert(self.fl[id] == -1)
        if self.count == 0:
            assert (self.head_id == 0 and self.tail_id == 0)
            self.head_id = self.tail_id = id
            self.fl[id] = 0
            self.count+=1
            return 
        self.fl[self.tail_id] = id
        self.tail_id = id
        self.fl[id] = 0
        self.count+=1

        
    def print_free_list(self):
        tmp_head_id = self.head_id
        while tmp_head_id != 0:
            print tmp_head_id,
            tmp_head_id = self.fl[tmp_head_id]
    
if __name__=='__main__':
    idmap = FreeList(5)
    for i in range(5):
        print idmap.alloc(),
    print
    for i in range(1,4):
        idmap.recycle(i)
    idmap.print_free_list()
    print
    for i in range(6):
        print idmap.alloc(),
    print
    idmap.print_free_list()
    
      
        