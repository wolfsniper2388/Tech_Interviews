''' Implement API strstr()
    return the index in orig_str of the first occurrence of sub_str, -1 if sub_str is not in orig_str
    E.g
        Input: acdegcdfmop
        Output: cdf
'''

def strstr_1(orig_str, sub_str):
    if not sub_str:
        return orig_str
    # i will only increase 1 after for loop no matter how i changes inside loop
    for i in range(len(orig_str)):
        # if the length of the rest elements in orig_str is less than the length of sub_str
        # there is no match in the rest
        if len(orig_str) - i < len(sub_str):
            return -1
        if orig_str[i] == sub_str[0]:
            i+=1
            j=1
            while j < len(sub_str):
                if orig_str[i] != sub_str[j]:
                    break
                else:
                    i+=1
                    j+=1
            if j == len(sub_str):
                return i-j
    return -1

def strstr_2(orig_str, sub_str):
    i=j=0
    while i < len(orig_str) and j < len(sub_str):
        if orig_str[i] == sub_str[j]:
            i+=1
            j+=1
        else:
            # if mismatch, i goes back to i-j+1, j goes back 0
            i = i-j+1
            j = 0
    if j == len(sub_str):
        return i-j
    else:
        return -1
    

if __name__=='__main__':
    test_cases = [('accdfe','cdf'), ('abc', 'a'), ('ace', 'acef'), ('acdegcdfmop','egm'), ('abd', ''), ('ababacbac', 'abac')]
    for each_test_case in test_cases:
        orig_str, sub_str = each_test_case
        print orig_str, sub_str, strstr_1(orig_str, sub_str), strstr_2(orig_str, sub_str)
        