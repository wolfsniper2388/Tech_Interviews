''' find all permutations of a string
'''


''' find all permutations of my_str
    @param my_str: the passed in string
    @return: a list strings of all permutations of my_str
'''
def get_all_permutations(my_str):
    if len(my_str)==1:
        return [my_str]
    prev_str = my_str[:-1]
    last_element = my_str[-1]
    prev_result=get_all_permutations(prev_str)
    new_result=[]
    for each_prev_permutation in prev_result:
        for position in range(len(each_prev_permutation)+1):
            # insert last_element in each position
            new_string=each_prev_permutation[position:]+last_element+each_prev_permutation[:position]
            if new_string not in new_result:
                new_result.append(new_string)
    return new_result

if __name__=='__main__':
    test_cases = ['abc', 'aac', 'a']
    for each_test_case in test_cases:
        print each_test_case, get_all_permutations(each_test_case)