''' Given a string, find the length of the longest substring without repeating characters. 
    E.g 
        Input: 'abcabcbb'
        Output: 'abc'
        Input: 'bbbbb'
        Output: 'b'
'''

def find_longest_substring_no_repeating_chars(orig_str):
    ch_list = list(orig_str)
    ch_hash={}
    max_len=0
    max_start=0
    for i, ch in enumerate(ch_list):
        if ch not in ch_hash:
            # reverse hashing: hash char to its index
            ch_hash[ch] = i
        else:
            # update max_len if necessary
            max_len = max(max_len, i-max_start)
            old_start = max_start
            # can easily locate the index of previously occurred char: ch_hash[ch]
            # the new start will the index +1
            max_start = ch_hash[ch]+1
            # delete all the chars from old_start to max_start in hash table
            for ch in ch_list[old_start:max_start]:
                del ch_hash[ch]
            # update the index of current char to current index:i
            ch_hash[ch]=i
    curr_len = len(ch_list) - max_start
    if curr_len > max_len:
        return orig_str[max_start:]
    else:
        return orig_str[max_start:max_start+max_len]
    
if __name__=='__main__':
    test_strings=['bbbbbb', 'abcdcef', 'abcdcefgd']
    for each_test_string in test_strings:
        print each_test_string, find_longest_substring_no_repeating_chars(each_test_string)
    
                
            