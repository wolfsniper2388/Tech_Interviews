''' Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
'''

from Heap import Heap
from LinkList import *
import sys

def merge_lists(lists):
    ''' merge len(lists) sorted linked lists, and return the result linked list
    '''
    for each_list in lists:        
        each_list.append_node(ListNode(sys.maxint))
    min_heap = Heap()
    result_list = LinkList()
    curr_nodes = [each_list.head for each_list in lists]
    curr_datas = [node.data for node in curr_nodes]
    # build the heap according to curr_datas
    min_heap.build_heap('min', curr_datas)
    # min_heap.heap[0] == maxint means all the lists go to end, only then, stop the while loop
    while min_heap.heap[0] != sys.maxint:
        # extract min node
        curr_min = min_heap.extract_node()
        # append to result
        result_list.append_node(ListNode(curr_min))
        min_index = curr_datas.index(curr_min)
        curr_nodes[min_index] = curr_nodes[min_index].next
        curr_datas[min_index] = curr_nodes[min_index].data
        # insert the extracted node's next's data, and re-heapify
        min_heap.add_node(curr_datas[min_index])
    return result_list

if __name__=='__main__':
    lists=[[2,5,8], [1,4,10], [3,6,7]]
    linklists=[]
    for each_list in lists:
        linklists.append(LinkList(each_list))
    for each_list in linklists:
        each_list.print_list()
    merge_lists(linklists).print_list()