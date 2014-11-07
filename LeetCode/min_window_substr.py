''' Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
    E.g.
        Input: S='ADOBECODEBANC', T= 'ABC'
        Output: 'BANC'
        Input: S='acbbaca' T = 'aba'
        Output: 'baca'
    Notice: if there is no such window in S that covers all characters in T, return the empty string
    if there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S
    
'''


def min_window_substr(S,T):
    ''' need_to_find is a table that records the occurrence of a character in T
        has_found records the occurrence of a character (that appears in T) in S met so far
        count is the total characters in T that has been met so far in S 
    '''
    need_to_find={}
    has_found={}
    count=0
    # create need_to_find table
    for ch in T:
        if ch not in need_to_find:
            need_to_find[ch]=1
        else:
            need_to_find[ch]+=1
    # initialize variable
    start = 0
    min_len=len(S)+1
    min_start=0
    min_end=-1
    
    for end in range(len(S)):
        x=S[end]
        # skip the characters in S that is not in T
        if x not in need_to_find:
            continue
        # update has_found table
        if x not in has_found:
            has_found[x]=1
        else:
            has_found[x]+=1
        # increment count only if has_found[x] <= nft[x] 
        if has_found[x] <= need_to_find[x]:
            count+=1
        # if window constraint is satisfied (each character in T has been met exactly the same times in S)
        # e.g. S='acbbaca', T='aba', the first window constraint is satisfied when end reaches 4
        if count == len(T):
            y=S[start]
            # start++ only when S[start] is not in T or has_found[S[start]] > need_to_find[S[start]] (S has met more S[start] than required)
            while y not in need_to_find or has_found[y] > need_to_find[y]:
                if y in need_to_find and has_found[y] > need_to_find[y]:
                    has_found[y]-=1
                start+=1
                y=S[start]
            # update minimum if necessary
            if end-start+1<min_len:
                min_start=start
                min_end=end
                min_len=end-start+1
                
    return S[min_start:min_end+1]

if __name__=='__main__':
    test_cases = [('acbbaca','aba'),('ADOBECODEBANC','ABC'), ('abc','d'),('a','a')]
    for each_test_case in test_cases:
        S,T= each_test_case
        print S,T,min_window_substr(S,T) 
                