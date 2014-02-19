''' Write a function to find the longest common prefix string amongst an array of strings.
'''

def find_longest_common_prefix(strs):
    if not strs:
        return ''
    pos = 0
    min_len = min([len(each_str) for each_str in strs])
    while pos < min_len:
        # curr_ch is value at pos of the first string in strs
        curr_ch = strs[0][pos]
        for each_str in strs[1:]:
            if each_str[pos] != curr_ch:
                return strs[0][:pos]
        pos+=1
    # 'while loop' ends, pos == min_len    
    return strs[0][:pos]

if __name__=='__main__':
    test_cases=[['abcd', 'abc', 'abcef'], ['', 'acd', 'acde'], ['wife', 'wifefg', 'wab', 'wb'],[]]
    for each_test_case in test_cases:
        print each_test_case, find_longest_common_prefix(each_test_case)
        