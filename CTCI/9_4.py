''' find all subsets of a set
'''

''' find all subsets of set
    means find all subsets of 
    @param my_set: the set (of list type)
    @return: a list of subsets of the set 
'''

from copy import deepcopy

def get_all_subsets(my_set):
    if len(my_set) == 0:
        return [[]]
    last_element=my_set[-1]
    # my_set[:-1] is the slice of my_set, excluding the last element
    # e.g. my_set=[1,3,5,6], my_set[:-1]=[1,3,5]
    prev_result=get_all_subsets(my_set[:-1])
    prev_result_size=len(prev_result)
    # make copy, !!! use deepcopy
    new_result=deepcopy(prev_result)+deepcopy(prev_result)
    #new_result=[subset for subset in prev_result]*2
    # append last_element to each first half set of last_result
    for each_subset in new_result[:prev_result_size]:
        each_subset.append(last_element)
    return new_result

if __name__=='__main__':
    a=[5,1,3,7]
    print get_all_subsets(a)