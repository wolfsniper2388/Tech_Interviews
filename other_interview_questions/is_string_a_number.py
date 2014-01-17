''' check if a string is a valid number
'''

def is_num(orig_str):
    ch_list = list(orig_str)
    dot_hash={}
    for i, ch in enumerate(ch_list):
        # + or - can only be at first
        if (ch == '+' or ch == '-') and i != 0:
            return False
        # + - . (0-9) are only valid chars
        if ch != '+' and ch != '-' and ch != '.' and (ch < '0' or ch > '9' ):
            return False
        # . can only occur once
        if ch == '.': 
            if ch not in dot_hash:
                dot_hash['.']=1
            else:
                return False
    return True

if __name__=='__main__':
    test_cases = ['+1-345.9.0', '1304ab.34', '-123.45', '124.7.90']
    for each_test_case in test_cases:
        print each_test_case, is_num(each_test_case)
        
            