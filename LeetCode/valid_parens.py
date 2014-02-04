''' Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    The brackets must close in the correct order, 
    E.g
        Input '()'
        Output: True 
        Input: '()[]{}' 
        Output: True
        Input:'(]'
        Output: False
        Input: '([)]'
        Output: False
'''
def is_match(paren_1, paren_2):
    if paren_1 == '(':
        return paren_2 == ')'
    if paren_1 == '[':
        return paren_2 == ']'
    if paren_1 == '{':
        return paren_2 == '}'
    
def is_left(paren):
    return paren=='(' or paren=='[' or paren=='{'

def is_right(paren):
    return paren==')' or paren==']' or paren=='}'

def is_parens_valid(parens):
    stack = []
    for paren in parens:
        # if left, push to stack
        if is_left(paren):
            stack.append(paren)
        elif is_right(paren):
            # if stack is empty, mismatch
            if not stack:
                return False
            # if match stack[top], pop top
            if is_match(stack[-1], paren):
                stack.pop()
            # else, mismatch
            else:
                return False
        # invalid input    
        else:
            raise KeyError
            return False
    # after the for loop, if the stack is not empty, return False, e.g. '('
    return False if stack else True
    
if __name__=='__main__':
    test_cases=[')', '(','([{}()])', '(]', '()[]{}(']
    for each_test_case in test_cases:
        print each_test_case, is_parens_valid(each_test_case)