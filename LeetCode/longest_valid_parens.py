''' Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
    E.g
        Input: '())((())())'
        Output: 8
        Input: '(()'
        Output: 2
''' 

def find_longest_valid_parens(parens):
    stack = []
    max_len = 0
    last_valid_index = 0
    for i in range(len(parens)):
        if parens[i] == '(':
            stack.append(i)
        else:
            if not stack:
                last_valid_index = i+1
            else:
                stack.pop()
                if not stack:
                    max_len = max(max_len, i - last_valid_index+1)
                else:
                    max_len = max(max_len, i - stack[-1])
    return max_len

if __name__=='__main__':
    test_cases = [')())(()))', '(()', '(', '())((())())', '()(()', '())(()())']
    for each_test_case in test_cases:
        print each_test_case, find_longest_valid_parens(each_test_case)