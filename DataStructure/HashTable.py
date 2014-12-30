''' Implement a hash table that supports O(1) lookup and O(1) insert in the best case
'''

class HashNode(object):
    def __init__(self, k , v):
        self.key = k
        self.value = v
        self.next = None
    def __repr__(self):
        return '%s(%r)' %(self.__class__.__name__, (self.key, self.value)) 


class HashTable(object):
    def __init__(self, n):
        # create a hash table of table size n
        self.size = n
        self.table = [None] * n
        
    def _hash_function(self, s):
        hash_val = 0
        for ch in s:
            hash_val  = abs(ord(ch) + (hash_val <<5) - hash_val)
        return hash_val % self.size
        
    def insert(self, k, v):
        # insert (k,v) pair to hash table, return 0 if success, -1 if a duplicate is found
        
        idx = self._hash_function(k)
        head = self.table[idx]
        while head:
            if head.key == k:
                return -1
            head = head.next
            
        node = HashNode(k,v)

        node.next = self.table[idx]
        self.table[idx] = node
        return 0
        
    def find(self, k):
        # look up k in hash table and return v
        
        idx = self._hash_function(k)
        head = self.table[idx]
        while head:
            if head.key == k:
                return head.value
            head = head.next
        return None
    
    
if __name__=='__main__':
    h = HashTable(1)
    d = [('yifei', 'cisco'),('yuqi','scu'),('michael','scu'),('yifei', 'vmware')]
    for t in d:
        k,v = t
        h.insert(k, v)
    for k in ['yifei','yuqi','michael']:
        print h.find(k)
        
        