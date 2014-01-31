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
    new_result = deepcopy(prev_result)
    for each_subset in deepcopy(prev_result):
        each_subset.append(last_element)
        if  each_subset not in prev_result:
            new_result.append(each_subset) 
    return new_result

if __name__=='__main__':
    test_cases= [[5,1,3,7], [1,2,2]]
    for each_test_case in test_cases:
        print each_test_case, get_all_subsets(sorted(each_test_case))