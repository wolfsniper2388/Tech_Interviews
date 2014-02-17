''' Evaluate the value of an arithmetic expression in Reverse Polish Notation.
    Valid operators are +, -, *, /. Each operand may be an integer or another expression.
    E.g.
        Input: ['2', '1', '+', '3', '*'] 
        Output: 9 (((2 + 1) * 3))
        Input: ['4', '13', '5', '/', '+'] 
        Ouput: 6 ((4 + (13 / 5)))
'''
from __future__ import division
def is_operator(ch):
    return ch == '+' or ch == '-' or ch == '*' or ch == '/'

def eval_rpn(rpn):
    num_stack = []
    for ch in rpn:
        if not is_operator(ch):
            num_stack.append(int(ch))
        else:
            first_operand = num_stack.pop()
            second_operand = num_stack.pop()
            if ch == '+':
                num_stack.append(second_operand+first_operand)
            elif ch == '-':
                num_stack.append(second_operand-first_operand)
            elif ch == '*':
                num_stack.append(second_operand*first_operand)
            elif ch == '/':
                num_stack.append(int(second_operand/first_operand))
                
    return num_stack[-1]

if __name__=='__main__':
    test_cases = [['2', '1', '+', '3', '*'], ['4', '13', '5', '/', '+'], ['2','1','+','4','2','-','*'],['10','6','9','3','+','-11','*','/','*','17','+','5','+'],['0','3','/']]
    for each_test_case in test_cases:
        print each_test_case, eval_rpn(each_test_case)