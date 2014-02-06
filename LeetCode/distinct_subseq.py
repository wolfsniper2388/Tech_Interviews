''' Given two strings S and T. Find the number of subsequences in S, such that the subsequence is same as T
    E.g.
        Input: S = 'rabbbit', T= 'rabbit'
        Output: 3 (rabb*it, rab*bit, ra*bbit)
'''


''' add a dummy char at the first of S and T to make them both index 1 based
    Take S='@rabbbit' and T = '@rabbit' as an example
    define match[i][j] to be the number of subseq in S[:j] such that the subseq is the same as T[:i]
    match[i][j]  = match[i][j-1] if S[j]!=T[i]
                 = match[i][j-1]+match[i-1][j-1] if S[j] == T[i]
    This is because match[i][j] must be at least match[i][j-1]
    after the loop the match matrix would be:
        @ r a b b b i t
    @   1 0 0 0 0 0 0 0
    r   0 1 1 1 1 1 1 1
    a   0 0 1 1 1 1 1 1
    b   0 0 0 1 2 2 2 2
    b   0 0 0 0 1 3 3 3
    i   0 0 0 0 0 0 3 3
    t   0 0 0 0 0 0 0 3
'''
def num_subseq(S,T):
    S='@'+S
    T='@'+T
    N = len(S)
    M = len(T)
    match = [[0 for j in range(N)] for i in range(M)]
    for j in range(N):
        match[0][j]=1
    for i in range(1,M):
        for j in range(i, N):
             match[i][j] = match[i][j-1] if S[j]!=T[i] else match[i][j-1]+match[i-1][j-1]
    return match[-1][-1]

if __name__=='__main__':
    test_cases= [('rabbbit', 'rabbit'),('abcde','ace'), ('a','b'), ('ccc','c')]
    for each_test_case in test_cases:
        S,T = each_test_case
        print num_subseq(S,T)
                 