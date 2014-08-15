''' pure storage buddy system bitmap
    Given a complete binary tree with nodes of values of either 1 or 0, the following rules always hold:
    (1) a node's value is 1 if and only if all its subtree nodes' values are 1
    (2) a leaf node can have value either 1 or 0
    Implement the following 2 APIs:
    set_bit(offset, length), set the bits at range from offset to offset+length-1
    clear_bit(offset, length), clear the bits at range from offset to offset+length-1
    
    i.e. The tree is like:
                 0
              /     \
             0        1
           /  \      /  \
          1    0    1    1
         /\   / \   / 
        1  1 1   0 1
        Since it's complete binary tree, the nodes can be stored in an array:
        [0,0,1,1,0,1,1,1,1,1,0,1]
        
'''

def setbit_down(A, x, n):
    if x>=n:
        return
    if 2*x+1<=n and A[2*x+1]==0:
        A[2*x+1]=1
        setbit_down(A,2*x+1,n)
    if 2*x+2<=n and A[2*x+2]==0:
        A[2*x+2]=1
        setbit_down(A,2*x+2,n)
    

def set_bit(A, pos, length):
    n = len(A)-1    #last index of A
    for x in range(pos, min(n,min(pos+length, 2*pos+1))):
        # set self
        A[x]=1
        # set descendants
        setbit_down(A,x, n)
        # set ancestors
        while x>0:
            if (x%2==0 and A[x-1]==1) or (x%2==1 and x<n and A[x+1]==1):
                A[(x-1)/2] = 1
            x = (x-1)/2
                
if __name__=='__main__':
    A=[0,0,1,1,0,1,1,1,1,1,0,1]
    set_bit(A,5,1)
    print A