''' find all permutations of a string
'''


''' find all permutations of s
    @param s: the passed in string
    @return: a set of strings consisting all permutations of s
'''
def get_all_permutations(s):
    if len(s)==1:
        return set([s])
    prev_str = s[:-1]
    last_element = s[-1]
    prev_result=get_all_permutations(prev_str)
    new_result=set()
    for each_prev_permutation in prev_result:
        for position in range(len(each_prev_permutation)+1):
            # insert last_element in each position
            new_string=each_prev_permutation[position:]+last_element+each_prev_permutation[:position]
            new_result.add(new_string)
    return new_result

if __name__=='__main__':
    test_cases = ['abc', 'aca', 'a']
    for each_test_case in test_cases:
        print each_test_case, get_all_permutations(each_test_case)