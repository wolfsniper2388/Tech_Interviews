''' Given a string containing only digits, restore it by returning all possible valid IP address combinations.
    E.g
        Input: '25525511135'
        Output: ['255.255.11.135', '255.255.111.35']. (Order does not matter)
'''

''' take 123456 as an example
    first we take 1 as the first part, then 2 as second part, 3 as third part
    determined_count == 3 now, we find 456 is invalid, trace back
    we take 34 as third part and find 56 can be a valid number, so we push 1.2.34.56 to result
    then we go back and take 345 as third part, this alone is not valid, then return
    we take 23 as second part, 4 as third part, determined_count == 3 now, we find 56 is valid we push 1.23.4.56 to result
    ...
'''

def restore_ip(s):
    result=[]
    restore_ip_dfs(s,'',result,0)
    return result
    
def is_valid(sub_str):
    if not sub_str:
        return False
    sub_int = int(sub_str)
    if sub_str[0] == '0':
        return sub_int==0
    return 0<sub_int<=255


''' 
    @param s: original ip string
    @param tmp: tmp result ip string
    @param result: a list of possible valid ip strings to be returned
    @param determined_count: how many parts have been determined yet, valid number is 0,1,2,3
'''
def restore_ip_dfs(s, tmp, result, determined_count):
    # determined_count ==3 means this is the 4th part, the previous 3 parts are now determined
    if determined_count == 3:
        # if 4th part can be a valid number, push tmp+s to result, else return
        if is_valid(s):
            result.append(tmp+s)
        return
    for i in range(1,4):
        if is_valid(s[:i]):
            restore_ip_dfs(s[i:], tmp+s[:i]+'.', result, determined_count+1)

if __name__=='__main__':
    test_cases = ['25525511135','122456','123456']
    for each_test_case in test_cases:
        print each_test_case, restore_ip(each_test_case)