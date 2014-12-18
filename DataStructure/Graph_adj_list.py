import sys
from heapq import *

# each GraphNode consists of its own data, its index in the array, and its key for the mst purpose
class GraphNode(object):
    def __init__(self, data, index):
        self.data = data
        self.index = index
        self.key = sys.maxint
        
    def __repr__(self):
        return '%s(%r)' %(self.__class__.__name__, (self.data, self.index, self.key))
    
    def __lt__(self, other):
        return self.key < other.key

# ArrayCell consists of GraphNode and AdjList
class ArrayCell(object):
    def __init__(self):
        self.graph_node = None
        self.adj_list = AdjList()

# AdjListNode consists of GraphNode, weight, and next
class AdjListNode(object):
    def __init__(self, dest, weight):
        self.dest = dest
        self.weight = weight
        self.next = None
    def __repr__(self):
        return '%s(%r)' %(self.__class__.__name__, (self.dest, self.weight))
    
# AdjList consists of a linked list of AdjListNode
class AdjList(object):
    def __init__(self):
        self.head = None
   
    def add_node_to_head(self, node):
        node.next = self.head
        self.head = node
    
    def print_list(self):
        p = self.head
        while p:
            print p, '->', 
            p = p.next
        print

class Graph(object):
    def __init__(self, n_vertex, indicator):
        self.n_vertex = n_vertex
        # array consists of n_vertex number of ArrayCell
        self.array = [None]*n_vertex
        for i in range(n_vertex):
            self.array[i] = ArrayCell()
        assert(indicator == 'directed' or indicator == 'undirected')
        self.indicator = indicator
        self.curr_n_vertex = 0
        
    def add_node(self, data):
        assert(self.curr_n_vertex < self.n_vertex)
        self.array[self.curr_n_vertex].graph_node = GraphNode(data, self.curr_n_vertex)
        self.curr_n_vertex += 1
        
    def add_edge(self, src_index, dest_index, weight):
        adj_list_node = AdjListNode(self.array[dest_index].graph_node, weight)
        self.array[src_index].adj_list.add_node_to_head(adj_list_node)
        
        if self.indicator == 'undirected':
            adj_list_node = AdjListNode(self.array[src_index].graph_node, weight)
            self.array[dest_index].adj_list.add_node_to_head(adj_list_node)            
    
    def print_graph(self):
        for i in range(self.n_vertex):
            print i, self.array[i].graph_node
            self.array[i].adj_list.print_list()
    
    def minimum_spanning_tree_prim(self):
        prev = [None] * self.n_vertex
        min_heap = []
        # mark the first node's key as 0, so it's picked by min heap at first
        self.array[0].graph_node.key = 0
        # put all the nodes to the min heap
        for i in range(self.n_vertex):
            heappush(min_heap, self.array[i].graph_node)
        while min_heap:
            u = heappop(min_heap)
            # go to u's adjacent list
            p = self.array[u.index].adj_list.head
            while p:
                # v is the u's neighbor node
                v = p.dest
                # current key is not optimal
                if v in min_heap and v.key > p.weight:
                    # record v's previous as u
                    prev[v.index] = u.index
                    # update v's key
                    v.key = p.weight
                # go to u's next neighbor
                p = p.next
            heapify(min_heap)
        return prev
            
if __name__=='__main__':
    ''' Let us create the following graph
          2    3
      (a)--(b)--(c)
       |   / \   |
     10| 8/   \5 |7
       | /     \ |
      (d)-------(e)
            1          
    '''
    
    g= Graph(5, 'undirected')
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    g.add_node('d')
    g.add_node('e')
    g.add_edge(0,1,2)   # a-b: 2
    g.add_edge(1,2,3)   # b-c: 3
    g.add_edge(2,4,7)   # c-e: 7
    g.add_edge(0,3,10)  # a-d: 10
    g.add_edge(1,3,8)   # b-d: 8
    g.add_edge(1,4,5)   # b-e: 5
    g.add_edge(3,4,1)   # d-e: 1
    
    #g.print_graph()
    results = g.minimum_spanning_tree_prim()
    
    for i in range(g.n_vertex):
        if results[i]!=None:
            print g.array[results[i]].graph_node.data,'-',g.array[i].graph_node.data
        