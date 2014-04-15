''' A message containing letters from A-Z is being encoded to numbers using the following mapping:
    'A' -> 1
    'B' -> 2
    ...
    'Z' -> 26
    Given an encoded message containing digits, determine the total number of ways to decode it.
    E.g
        Input: '2513'
        Output: 4 ([2,5,1,3], [25,1,3], [25,13], [2,5,13])
        Input: '12'
        Output: 2 ([1,2], [12])
'''


''' return if 'prev curr' is between 10-26
'''
def is_curr_and_prev_digits_decodable(prev, curr):
    return prev == '1' or ( prev == '2' and '0' <= curr <= '6') 

''' return if curr is not '0'
'''
def is_curr_digit_decodable(curr):
    return curr != '0'

''' ways[i] = ways[i-1] if curr_digit is decodable and prev_digit and curr_digit combined are not decodable
            = ways[i-1] + ways[i-2] if curr_digit is decodable and prev_digit and curr_digit combined are also decodable
'''
def decode_ways(s):
    if not s:
        return 0
    ways = [0 for i in range(len(s))]
    ways[0]=is_curr_digit_decodable(s[0])
    if ways[0]==0:
        return 0;
    way1=is_curr_digit_decodable(s[1])
    way2=is_curr_and_prev_digits_decodable(s[0],s[1])
    ways[1]=way1+way2
    
    for i in range(2, len(s)):
        way1=way2=0
        # if curr digit is decodable
        if is_curr_digit_decodable(s[i]):
            way1 = ways[i-1]
        if is_curr_and_prev_digits_decodable(s[i-1],s[i]):
            way2 = ways[i-2]
        ways[i] = way1 + way2
        if ways[i]==0:
            return 0
        
    return ways[-1]

if __name__=='__main__':
    test_cases = ['12', '2513', '3','2626', '303', '00']
    for each_test_case in test_cases:
        print each_test_case, decode_ways(each_test_case)
        