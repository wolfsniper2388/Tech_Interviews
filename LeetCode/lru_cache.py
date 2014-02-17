''' Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.
    get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
    set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, 
    it should invalidate the least recently used item before inserting a new item.
'''

class Node(object):
    def __init__(self, k,v):
        self.key = k
        self.value = v
        self.prev = None
        self.next = None
    def __repr__(self):
        return '%s%r' %(self.__class__.__name__, (self.key, self.value))
        

class LRU(object):
    def __init__(self, capacity):
        self.capcity = capacity
        self.map = {}   # key <=> node
        self.head = None    # oldest        
        self.tail = None    # newest
    
    def __repr__(self):
        return '%s%r' %(self.__class__.__name__, self.map)
    
    def append_node(self, new_node):
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    
    def remove_head(self):
        tmp = self.head
        
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        print 'remove', tmp
        del tmp
    
    def move_node_to_tail(self, curr_node):
        if curr_node == self.tail:
            return
        if curr_node == self.head:
            self.head = curr_node.next
            curr_node.next.prev=None
        else:
            curr_node.prev.next = curr_node.next
            curr_node.next.prev = curr_node.prev
        self.tail.next = curr_node
        curr_node.prev = self.tail
        self.tail = curr_node
        curr_node.next = None
    
    
        
    def get(self, key):
        if key not in self.map:
            return -1
        curr_node = self.map[key]
        self.move_node_to_tail(curr_node)
        return self.map[key].value
            
        
    def set(self, key, value):
        if key in self.map:
            curr_node = self.map[key]
            self.move_node_to_tail(curr_node)
            self.map[key].value = value
        else:
            if len(self.map) == self.capcity:
                print 'max capacity reached'
                self.remove_head()
                self.map.pop(self.head.key)
            new_node = Node(key, value)
            self.append_node(new_node)
            self.map[key] = new_node
                
    
    

if __name__=='__main__':
    lru = LRU(4)
    print '36,10'
    lru.set(36, 10)
    print lru.head
    print lru.tail
    print '25,20'
    lru.set(25, 20)
    print lru.head
    print lru.tail
    print '76,30'
    lru.set(76, 30)
    print lru.head
    print lru.tail
    print '97,40'
    lru.set(97, 40)
    print lru.head
    print lru.tail
    print '36,12'
    lru.set(36, 12)
    print lru.head
    print lru.tail
    print 'get 36'
    print lru.get(36)
    print lru.head
    print lru.tail
    lru.set(52, 50)

    
