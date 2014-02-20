''' Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.

'''
class GraphNode(object):
    def __init__(self, data):
        self.data = data
        self.neighbors = []
        
from collections import deque
def clone_graph(start_node):
    map ={}
    q=deque()
    start_copy = GraphNode(start_node.data)
    map[start_node] = start_copy
    q.append(start_node)
    while q:
        curr_node = q.popleft()
        for next_node in curr_node.neighbors:
            # if neighbor not exist in map yet
            if next_node not in map:
                next_copy = GraphNode(next_node.data)
                map[next_node] = next_copy
                map[curr_node].neighbors.append(next_copy)
                q.append(next_node)
            else:
                map[curr_node].neighbors.append(map[next_node])
    return start_copy