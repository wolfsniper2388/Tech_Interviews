''' Q1.
    Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end, such that:
    Only one letter can be changed at a time
    Each intermediate word must exist in the dictionary
    E.g.
        Input: start='hit', end='cog', dict = ['hot','dot','dog','lot','log']
        Output: 5
    
    Q2.
    Instead of shortest lenght, find all shortest transformation sequence(s) from start to end
    E.g.
        Input: start='hit', end='cog', dict = ['hot','dot','dog','lot','log']
        Output: [['hit','hot','dot','dog','cog'],['hit','hot','lot','log','cog']]
'''

from collections import deque

def word_ladder_len(start, end, dictionary):
    if start==end:
        return 0
    # just like level order traversal in BinaryTree
    n_curr_level_words = 1
    n_next_level_words = 0
    d=set(dictionary)
    q = deque()
    visited = set()
    q.append(start)
    visited.add(start)
    min_len=0
    while q:
        s=q.popleft()
        n_curr_level_words-=1
        # i is each position in s
        for i in range(len(s)):
            # try to replace the curr_pos with chr(97+j)
            for j in range(26):
                tmp = list(s)
                tmp[i] = chr(97+j)
                tmp = ''.join(tmp)
                if tmp == end:
                    return min_len+2
                if tmp in d and tmp not in visited:
                    q.append(tmp)
                    visited.add(tmp)
                    n_next_level_words+=1
        if n_curr_level_words == 0:
            min_len+=1
            n_curr_level_words = n_next_level_words
            n_next_level_words =0 
    return 0

if __name__=='__main__':
    test_cases = [('hit','cog',['hot','dot','dog','lot','log'])]
    for each_test_case in test_cases:
        start, end, dictionary = each_test_case
        print start,end,dictionary,word_ladder_len(start,end,dictionary)              
                    
                    