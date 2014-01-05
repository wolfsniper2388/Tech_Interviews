'''	Implement a directional graph with edge weight
'''
from pprint import pprint
from collections import deque

class Graph:
    def __init__(self,vnumber):
        self.vertex_num=vnumber
        self.edge_num=0
        self.vertex_list=[]
        self.edge_matrix=[[0 for i in range (self.vertex_num)] for j in range (self.vertex_num)]
            
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
    
    def add_edge(self, vertex1,vertex2,cost):
        if vertex1==vertex2 or vertex1 not in self.vertex_list or vertex2 not in self.vertex_list:
            print 'Cannot add edge! Please check input'
            return
        vertex1_index=self.vertex_list.index(vertex1)
        vertex2_index=self.vertex_list.index(vertex2)
        if self.edge_matrix[vertex1_index][vertex2_index] !=0:
            print 'The edge already exists. Cannot add edge', (vertex1,vertex2,cost)
            return
        self.edge_matrix[vertex1_index][vertex2_index]=cost
    def print_graph(self):
        pprint(self.edge_matrix)
        
    def dfs(self, start_vertex):
        if start_vertex not in self.vertex_list:
            print start_vertex,' is not in vertex_list'
            return
        start_vertex_index=self.vertex_list.index(start_vertex)
        visited=set()
        self.dfs_helper(start_vertex_index,visited)
        
    def dfs_helper(self,current_index,visited):
        print self.vertex_list[current_index],
        visited.add(current_index)
        # search for all the vertices adjacent that has not been visited 
        for next_index in range(self.vertex_num):
            if next_index not in visited and self.edge_matrix[current_index][next_index]!=0:      
                self.dfs_helper(next_index,visited)
                
    def bfs(self,start_vertex):
        q=deque([])
        start_index=self.vertex_list.index(start_vertex)
        q.append(start_index)
        visited=set()
        while q:
            current_index=q[0]
            visited.add(current_index)
            for next_index in range(self.vertex_num):
                if self.edge_matrix[current_index][next_index]!=0 and next_index not in visited:
                    q.append(next_index)
            print self.vertex_list[current_index],
            q.popleft()
            
    #def is_connected(self, vertex1, vertex2):
        
if __name__=='__main__':
    ''' The graph is          
        >f-->g<--h
      /   \ 
     /      >
    a<---d-->e 
    |    ^  
    >    |
    b--> c
         ^
         |
         i
    '''
    g=Graph(9)
    for ch in ['a','b','c','d','e','f','g','h','i']:
        g.add_vertex(ch)
    g.add_edge('a','b',1)
    g.add_edge('b','c',1)
    g.add_edge('c','d',1)
    g.add_edge('d','a',1)
    g.add_edge('a','f',1)
    g.add_edge('f','g',1)
    g.add_edge('f','e',1)
    g.add_edge('h','g',1)
    g.add_edge('d','e',1)
    g.add_edge('i','c',1)

    g.print_graph()
    
    print 'Testing DFS'
    g.dfs('d')
    print '\nTesting BFS'
    g.bfs('d')