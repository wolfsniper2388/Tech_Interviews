'''    Implement a directional graph with edge weight using adjacent matrix
'''
from pprint import pprint
from collections import deque
import sys

class GraphNode(object):
    def __init__(self, data):
        self.data = data
    
    def __repr__(self):
        return '%s(%r)' %(self.__class__.__name__, self.data)

class Graph:
    def __init__(self,vnumber, indicator):
        self.vertex_num=vnumber
        self.edge_num=0
        self.vertex_list=[]
        self.edge_matrix=[[0 for i in range (self.vertex_num)] for j in range (self.vertex_num)]
        assert(indicator == 'directed' or indicator == 'undirected')
        self.indicator = indicator
            
    def __repr__(self):
        return '%s(%r)' %(self.__class__.__name__, self.vertex_list)

    def add_vertex(self, vertex):
        current_vertex_number=len(self.vertex_list)
        if vertex in self.vertex_list:
            print vertex, 'already in in the vertex_list. Cannot add vertex'
            return
        if current_vertex_number==self.vertex_num:
            print 'Vertex list is full. Cannot add vertex'
            return
        self.vertex_list.append(vertex)
    
    def add_edge(self, vertex1_index,vertex2_index,cost):
        assert 0 <= vertex1_index < len(self.vertex_list) and 0 <= vertex2_index < len(self.vertex_list)
        if self.edge_matrix[vertex1_index][vertex2_index] != 0:
            print 'The edge already exists. Cannot add edge', (self.vertex_list[vertex1_index],self.vertex_list[vertex2_index],cost)
            return
        self.edge_matrix[vertex1_index][vertex2_index]=cost
        if self.indicator == 'undirected':
            self.edge_matrix[vertex2_index][vertex1_index]=cost
    
    def print_graph(self):
        pprint(self.edge_matrix)
        
    def dfs(self, start_vertex_index):
        if start_vertex_index <0 or start_vertex_index>len(self.vertex_list):
            print start_vertex_index,' invalid'
            return
        visited=set()
        self.dfs_helper(start_vertex_index,visited)
        
    def dfs_helper(self,curr_index,visited):
        print self.vertex_list[curr_index],
        visited.add(curr_index)
        # search for all the vertices adjacent that has not been visited 
        for next_index in self.get_neighbors_indices(curr_index):
            if next_index not in visited:      
                self.dfs_helper(next_index,visited)
                
    def bfs(self,start_vertex_index):
        q=deque([])
        q.append(start_vertex_index)
        visited=set()
        visited.add(start_vertex_index)
        while q:
            curr_index=q.popleft()
            print self.vertex_list[curr_index],
            for next_index in self.get_neighbors_indices(curr_index):
            #for next_index in range(self.vertex_num):
                if next_index not in visited:
                    visited.add(next_index)
                    q.append(next_index)
            
    
    def get_neighbors_nodes(self, vertex_index):
        'return a list of nodes that are neighbors of vertex_list[vertex_index]'
        return [self.vertex_list[i] for i in range(len(self.vertex_list)) if self.edge_matrix[vertex_index][i]!=0]
    
    def get_neighbors_indices(self, vertex_index):
        'return a list of indices that are neighbors of vertex_index'
        return [i for i in range(len(self.vertex_list)) if self.edge_matrix[vertex_index][i]!=0]
    #def is_connected(self, vertex1, vertex2):
        
        
if __name__=='__main__':
    ''' The graph is          
    
        >f-->g<--h
      /   \ 
     /      >
    a<---d-->a 
    |    ^  
    >    |
    b--> c
         ^
         |
         i
    '''
    g=Graph(9, 'undirected')
    for ch in ['a','b','c','d','a','f','g','h','i']:
        g.add_vertex(GraphNode(ch))
    g.add_edge(0,1,1)   # 'a'->'b'
    g.add_edge(1,2,1)   # 'b'->'c'
    g.add_edge(2,3,1)   # 'c'->'d'
    g.add_edge(3,4,1)   # 'd'->'a'
    g.add_edge(0,5,1)   # 'a'->'f'
    g.add_edge(5,6,1)   # 'f'->'g'
    g.add_edge(5,4,1)   # 'f'->'a'
    g.add_edge(7,6,1)   # 'h'->'g'
    g.add_edge(3,0,1)   # 'd'->'a'
    g.add_edge(8,2,1)   # 'i'->'c'

    g.print_graph()
    
    print 'Testing DFS'
    g.dfs(3)
    print '\nTesting BFS'
    g.bfs(3)
    
    print '\nTesting get_neighbors'
    for vertex_index in range(9):
        print vertex_index, g.get_neighbors_nodes(vertex_index)
        print vertex_index, g.get_neighbors_indices(vertex_index)