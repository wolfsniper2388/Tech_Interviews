''' You are given a string, S, and a list of words, L, that are all of the same length. 
    Find all starting indices of substring(s) in S that is a concatenation of each word in L exactly once
    and without any intervening characters.
    E.g.
        Input: S='aaaaabcaaa' T = ['aa','aa','bc']
        Output: [1,3]
'''
from copy import deepcopy
def find_substr(S,T):
    map={}
    result=[]
    for each_str in T:
        if each_str not in map:
            map[each_str] = 1
        else:
            map[each_str]+=1
    map_copy=deepcopy(map)
    n=len(S)
    m=len(T)
    word_len = len(T[0])
    ''' start = 0,1,2,... n-m*word_len
        for each start, have a window of length m*word_len,
        check within the window, if each word in T appears exactly once
        then move the window to right by one
    ''' 
    for start in range(n-m*word_len+1):
        each_start = start
        while each_start <= start+(m-1)*word_len:
            each_substr=S[each_start: each_start+word_len]
            if each_substr in map and map[each_substr]>0:
                map[each_substr]-=1
                each_start+=word_len
            else: 
                break
        if each_start == start+m*word_len:
            result.append(start)
        map=deepcopy(map_copy)
        
    return result


if __name__=='__main__':
    test_cases=[('aaaaabcaaa',['aa','aa','bc']),('mississipi', ['is','si'])]
    for each_test_case in test_cases:
        S,T=each_test_case
        print S,T,find_substr(S,T)
        