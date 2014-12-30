''' Implement a min/max Heap
    Supported action:
        build_heap
        heapify
        add_node
        extract_node
        heap_sort
'''
import copy

class Heap(object):
    def __init__(self):
        self.heap=[]
        self.indicator=None
    
    def __repr__(self):
        return '%s(%r)' %(self.__class__.__name__, self.heap)
    
    ''' 
         @param indicator: 'min': min heap or 'max': max heap
         @param seq:        sequence
    '''
    def build_heap(self, indicator, seq):
        assert indicator == 'max' or indicator == 'min'
        # whenever user called build_heap, remember the user choice of indicator
        self.indicator=indicator
        #deepcopy will seperate seq from self.heap, else they will be the same all the time
        self.heap=copy.deepcopy(seq)
        for subroot in range(len(self.heap)/2-1,-1,-1):
            self.heapify(subroot)
        # the sequence is maintained by the Heap class
        #self.heap=seq
        
    ''' 
        @param subroot:    index of the root of the subtree to be heapified
        Implement the action of heapify
            Ensure the subtree under the subroot is heapified
        
    ''' 
    def heapify(self, subroot):
        left_child=subroot*2+1
        right_child=subroot*2+2
        # tag stands for minimum of the subroot, left_child and right_child if indicator is 'min' 
        # and maximum 'max'
        tag=0
        if self.indicator == 'min':
            if (left_child<len(self.heap) and self.heap[subroot]>self.heap[left_child]):
                tag=left_child
            else:
                tag=subroot
            if (right_child<len(self.heap) and self.heap[tag]>self.heap[right_child]):
                tag=right_child
                
        # indicator is 'max'
        else:
            if (left_child<len(self.heap) and self.heap[subroot]<self.heap[left_child]):
                tag=left_child
            else:
                tag=subroot
            if (right_child<len(self.heap) and self.heap[tag]<self.heap[right_child]):
                tag=right_child
                
        if tag!=subroot:
            self.heap[subroot],self.heap[tag]=self.heap[tag], self.heap[subroot]
            self.heapify(tag)

    
    ''' 
        Implement the action of adding a node to heap:
            if min heap:
                if the inserted one is smaller than its parent: sift up
                else do nothing
            if max heap:
                if the inserted one is larger than its parent: sift up
                else do nothing
    '''
    def add_node(self,x):
        self.heap.append(x)
        self.sift_up(len(self.heap)-1)
    
    def sift_up(self, node_index):
        if node_index!=0:
            parent_index=(node_index-1)/2
            if self.indicator=='min':
                if self.heap[parent_index]>self.heap[node_index]:
                    self.heap[parent_index],self.heap[node_index]=self.heap[node_index],self.heap[parent_index]
                    self.sift_up(parent_index)
            else:
                if self.heap[parent_index]<self.heap[node_index]:
                    self.heap[parent_index],self.heap[node_index]=self.heap[node_index],self.heap[parent_index]
                    self.sift_up(parent_index)
    
    '''
         @return: root
         Implement the action of extracting the root from heap
         assign the root to be heap[last_index]
         heap_size--
         re heapify the heap
    '''
    def extract_node(self):
        root=self.heap[0]
        self.heap[0]=self.heap[-1]
        self.heap.pop()
        self.heapify(0)
        return root
    
    '''
        @param indicator:    'min': ascending sort, 'max': descending sort
        @param seq:            the sequence to be sorted
        @return: sorted_seq:    the sorted sequence
        build the heap
        extract the root from the heap until heap is empty
    '''
    
    def heap_sort(self,indicator,seq):
        sorted_seq=[]
        self.build_heap(indicator, seq)
        while self.heap:
            sorted_seq.append(self.extract_node())
        return sorted_seq
    
    
    ''' get an array consisting of k smallest/largest numbers in seq
        assume the first k numbers in seq are the minimum/maximum numbers
            1. maintain a max/min (opposite, i.e if output k smallest numbers in seq, maintain a max heap, and vice versa)
            heap of size k
            2. loop over the rest len(seq)-k numbers in seq:
            3.     if number is smaller/larger than the heap root, assign heap root to number
            4.     re-heapify
            5. return the heap
        The time complexity is O(N*logk), where N=len(seq)    
    '''
    def get_kth(self,indicator,seq,k):
        if indicator == 'min':
        # build a max heap, and assume initially the heap consists of the minimum k numbers of seq
            self.build_heap('max', seq[:k])
            for number in seq[k:]:
                if number < self.heap[0]:
                    self.heap[0] = number
                    self.heapify(0)
        else:
            # build a min heap, and assume initially the heap consists of the maximum k numbers of seq
            self.build_heap('min', seq[:k])
            for number in seq[k:]:
                if number > self.heap[0]:
                    self.heap[0] = number
                    self.heapify(0)
        return self.heap
                
            
    def print_heap(self):
        print self.heap

if __name__=='__main__':
    h=Heap()
    seq=[7,9,3,1,10,2,5,4,6]
    h.build_heap('min', seq)
    print 'The heap is'
    h.print_heap()    
    print 'After build_heap, the original seq is'
    print seq
    h.add_node(8)
    print 'After add node, the heap is'
    h.print_heap()
    print 'Root extracted is',h.extract_node()
    print 'After extracting root, the heap is', 
    h.print_heap()
    
    print 'Descending sort original seq'
    print h.heap_sort('max', seq)
    
    print 'Ascending sort original seq'
    print h.heap_sort('min', seq)
    
    print 'Get samllest kth'
    print h.get_kth('min', seq, 4)
    
    print 'Get largest kth'
    print h.get_kth('max', seq, 4)