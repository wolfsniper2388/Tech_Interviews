''' check if a string is a valid number
    check the finite state machine at http://blog.csdn.net/kenden23/article/details/18696083
'''

class Input_Type:
    invalid = 0
    space = 1
    sign =  2
    digit = 3
    dot = 4
    exp = 5
    
    

def is_num(orig_str):
                        #     space    sign  digit  dot   exp
    transition_matrix = [[-1,    0  ,    3,    1,    2,   -1],  # state 0
                         [-1,    8,     -1,    1,    4,    5],  # state 1    digit
                         [-1,   -1,     -1,    4,   -1,   -1],  # state 2    .
                         [-1,   -1,     -1,    1,    2,   -1],  # state 3    +/-
                         [-1,    8,     -1,    4,   -1,    5],  # state 4    digit .
                         [-1,   -1,      6,    7,   -1,   -1],  # state 5
                         [-1,   -1,     -1,    7,   -1,   -1],  # state 6
                         [-1,    8,     -1,    7,   -1,   -1],  # state 7
                         [-1,    8,     -1,   -1,   -1,   -1],  # state 8
                         ]
    
    state = 0
    for ch in orig_str:
        input_type = Input_Type.invalid
        if ch == ' ':
            input_type = Input_Type.space
        elif ch == '+' or ch == '-':
            input_type = Input_Type.sign
        elif '0'<= ch <='9':
            input_type = Input_Type.digit
        elif ch == '.':
            input_type = Input_Type.dot
        elif ch == 'e' or ch == 'E':
            input_type = Input_Type.exp
        state = transition_matrix[state][input_type]
        if state == -1:
            return False
    return state in [1, 4, 7, 8] 

if __name__=='__main__':
    test_cases = ['+1-345.9.0', '1304ab.34', '-123.45', '124.7.90', '3.']
    for each_test_case in test_cases:
        print each_test_case, is_num(each_test_case)
        
            