''' Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
    E.g.
        Input: 'aabcc', 'dbbca', 'aadbbcbcac'
        Output: True
        Input: 'aabcc', 'dbbca', 'aadbbbaccc'
        Output: False
'''


''' Let s1 = a1,a2...ai-2, ai ...
        s2 = b1,b2...bj-2, bj ...
        s3 = c1,c2...    ,ci+j-1,ci+j, ...
    define M[i][j] to be true if a1~ai and b1~bj match c1~ci+j
    then if ai == ci+j, then M[i][j]=M[i-1][j]
         if bj == ci+j, then M[i][j]=M[i][j-1]
         else: M[i][j] = False
    So using Dynamic Programming
    M[i][j] = (s1[i]==s3[i+j] and M[i-1][j] ) or  (s1[j]==s3[i+j] and M[i][j-1] )
    add a dummy char to s1,s2,s3 to make them 1 based
    Initially
    M[0][0] = True
    M[i][0] = True if s1[i] == s3[i]
    M[0][j] = True if s2[j] == s3[j]
    
    Suppose s1 = '@aabcc'
            s2 = '@dbbca'
    now i=2, j=3, s1[i]='a', s2[j]='b'
    match[2][3] means it will check if s1[:2]+s2[:3] will match s3[5]
    now s2[3] == s3[5], so match[2][3] = match[2][2]

'''
def is_interleave_1(s1,s2,s3):
    if len(s3) != len(s1)+len(s2):
        return False
    s1 = '@'+s1
    s2 = '@'+s2
    s3 = '@'+s3
    match = [[0 for j in range(len(s2))] for i in range(len(s1))]
    for j in range(1, len(s2)):
        if s2[j] == s3[j]:
            match[0][j] = 1
    for i in range(1, len(s1)):
        if s1[i] == s3[i]:
            match[i][0] = 1
            
    for i in range(1, len(s1)):
        for j in range(1, len(s2)):
            if s1[i] == s3[i+j]:
                match[i][j] = match[i-1][j]
            elif s2[j] == s3[i+j]:
                match[i][j] = match[i][j-1]
            else:
                match[i][j] = 0 
                
    return match[-1][-1]

def helper(s1,s2,s3,i,j,k):
    if k==-1:
        return True
    if (i>=0 and s3[k] == s1[i]) and not (j>=0 and s3[k] == s2[j]):
        return helper(s1,s2,s3,i-1,j,k-1)
    elif not (i>=0 and s3[k] == s1[i]) and (j>=0 and s3[k] == s2[j]):
        return helper(s1,s2,s3,i,j-1,k-1)
    elif (i>=0 and s3[k] == s1[i]) and (j>=0 and s3[k] == s2[j]):
        return helper(s1,s2,s3,i-1,j,k-1) or helper(s1,s2,s3,i,j-1,k-1)
    else:
        return False;

def is_interleave_2(s1,s2,s3):
    if len(s1)+len(s2)!=len(s3):
        return False
    return helper(s1,s2,s3,len(s1)-1, len(s2)-1, len(s3)-1)



if __name__=='__main__':
    test_cases = [('aabcc','dbbca','aadbbcbcac'), ('aabcc','dbbca','aadbbbaccc'), ('a','b','ba'), ('a','b','cd')]
    for each_test_case in test_cases:
        s1,s2,s3 = each_test_case
        print 'Solution 1'
        print s1,s2,s3,is_interleave_1(s1,s2,s3)
        print 'Solution 2'
        print s1,s2,s3,is_interleave_2(s1,s2,s3)