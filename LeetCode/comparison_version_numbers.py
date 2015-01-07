'''
'''

def compare_version_numbers(v1, v2):
    i = j =0
    len_v1 = len(v1)
    len_v2 = len(v2)
    
    while i < len_v1 or j < len_v2:
        n1 = n2 =0
        while i < len_v1 and v1[i] != '.':
            n1 = n1*10 + ord(v1[i]) - ord('0')
            i += 1
        while j < len_v2 and v2[j] != '.':
            n2 = n2*10 + ord(v2[j]) - ord('0')
            j += 1
            
        if n1 < n2:
            return -1
        elif n1 > n2:
            return 1
            
        i += 1
        j += 1
            
    return 0

if __name__=='__main__':
    test_cases = [('1.0','1.1'), ('1','1'),('10.0.1','10'), ('1','0'), ('1.23.45','12.4.7')]
    for each_test_case in test_cases:
        v1,v2 = each_test_case
        result = compare_version_numbers(v1,v2)
        if result == 1:
            print v1, '>', v2
        elif result == 0:
            print v1, '==', v2
        else:
            print v1, '<', v2

