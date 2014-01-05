''' find all permutations of a string
'''


''' find all permutations of my_str
    @param my_str: the passed in string
    @return: a list strings of all permutations 
'''
def get_all_permutations(my_str):
    if len(my_str)==1:
        return [my_str]
    # string->list
    my_str_list=list(my_str)
    # get last one
    last_element=my_str_list[-1]
    # list->string
    prev_str=''.join(my_str_list[:-1])
    prev_result=get_all_permutations(prev_str)
    new_result=[]
    for each_prev_permutation in prev_result:
        for position in range(len(each_prev_permutation)+1):
            # insert last_element in each position
            new_string=each_prev_permutation[position:]+last_element+each_prev_permutation[:position]
            new_result.append(new_string)
    return new_result

if __name__=='__main__':
    my_str='abc'
    print get_all_permutations(my_str)