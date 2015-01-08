'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

['((()))', '(()())', '(())()', '()(())', '()()()']
'''

def generate_parens(n):
    curr_result = []
    results = []
    generate_parens_helper(curr_result, results, n, n)
    return results

def generate_parens_helper(curr_result, results, left_remain, right_remain):
    if left_remain == 0 and right_remain == 0:
        results.append(''.join(curr_result))
        return results
    
    if left_remain > 0:
        curr_result.append('(')
        generate_parens_helper(curr_result, results, left_remain-1, right_remain)
        curr_result.pop()
    
    if left_remain < right_remain:
        curr_result.append(')')
        generate_parens_helper(curr_result, results, left_remain, right_remain-1)
        curr_result.pop()
    
if __name__ == '__main__':
    test_cases = [1,2,3]
    for each_test_case in test_cases:
        print each_test_case, generate_parens(each_test_case)