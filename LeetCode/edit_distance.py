''' Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. 
    (each operation is counted as 1 step.)
    You have the following 3 operations permitted on a word:
    a) Insert a character
    b) Delete a character
    c) Replace a character
'''


''' Idea: Dynamic Programming
    d[i][j] = min (d[i-1][j], d[i][j-1], d[i-1][j-1])+1
'''
def edit_distance(s ,t):
    m = len(s)
    n = len(t)
    d = [[0 for j in range (n+1)] for i in range(m+1)]
    
    for j in range(n+1):
        d[0][j] = j
    for i in range(m+1):
        d[i][0] = i
    
    for i in range (1,m+1):
        for j in range(1,n+1):
            # s ant t are 0 based so check s[i-1] and t[j-1] instead of s[i] and t[j]
            if s[i-1] == t[j-1]:
                d[i][j] = d[i-1][j-1]
            else:
                d[i][j] = min(d[i-1][j],     # should insert
                          d[i][j-1],         # should delete
                          d[i-1][j-1]        # should replace
                          )+1
    return d[m][n]

if __name__=='__main__':
    test_cases = [('sitting','kitten'), ('sunday','saturday'), ('abc', 'abc'), ('ade','')]
    for each_test_case in test_cases:
        s,t = each_test_case
        print s,t,edit_distance(s,t)