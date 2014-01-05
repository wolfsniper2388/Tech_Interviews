''' implement an algorithm to print all valid combinations of n-pairs of parentheses
    e.g
        input: 3
        output: ['((()))','(()())','()()()','()(())','(())()']
    
'''

''' 
    @param paren_list: the list of parens to return e.g. ['((()))','(()())','()()()','()(())','(())()']
    @param left_remain: left parens remaining
    @param right_remain: right parens remaining
    @param paren_str: one valid paren combo in the return list, e.g. ['(','(','(',')',')',')']
    @param pos: the position to insert in the paren_str in each recursion
    @return: void
    
    ideas:
        as long as left parens are not drained (left_remain > 0), we can always insert a left paren at paren_str[pos]
        as long as no syntax error like [')','('], we can always insert a right paren at paren_str[pos], we conclude that
        no syntax error <=> right parens in use < left parens in use (right_remain > left_remain)
'''

def add_paren(paren_list, left_remain, right_remain, paren_str, pos):
    # invalid
    if left_remain<0 or right_remain<left_remain:
        return
    
    # all the parens are used, add the paren_str (convert from list to string first) to paren_list 
    if left_remain==0 and right_remain==0:
        paren_list.append(''.join(paren_str))
        return
    
    if left_remain > 0:
        paren_str[pos]='('
        add_paren(paren_list, left_remain-1, right_remain, paren_str, pos+1)
        
    if right_remain > left_remain:
        paren_str[pos]=')'
        add_paren(paren_list, left_remain, right_remain-1, paren_str, pos+1)
    
    
def generate_parentheses(n):
    paren_list=[]
    paren_str=[None]*2*n
    add_paren(paren_list, n, n, paren_str, 0)
    return paren_list



if __name__=='__main__':
    print generate_parentheses(3)    