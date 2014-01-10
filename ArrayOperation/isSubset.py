''' Given two sorted array a and b, check if b is a subset of a
    space complexity is O(1)
'''

def is_subset(a,b):
    # i: index of a, j index of b
    i=j=0
    while j<len(b):
        while a[i] < b[j] and i < len(a)-1: 
            i+=1
        if a[i] != b[j]:
            break
        # deal with a[i]==b[j]
        i+=1
        j+=1
    if j == len(b):
        return True
    else:
        return False
    
    
if __name__=='__main__':
    print is_subset([1,4,6,6,9],[1,6,6])
    print is_subset([1,4,6,6,9],[1,6,9])
    print is_subset([1,4,6,6,9],[1,6,10])