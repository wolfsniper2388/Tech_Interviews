''' Implement merge sort
'''

def merge(seq_1,seq_2):
    '''
    i=0
    j=0
    seq=[]
    len_1=len(seq_1)
    len_2=len(seq_2)
    seq_1.append(float("infinity"))
    seq_2.append(float("infinity"))
    while i<len_1 or j<len_2:
        if seq_1[i]<seq_2[j]:
            seq.append(seq_1[i])
            i+=1
        else:
            seq.append(seq_2[j])
            j+=1
    return seq
    '''
    seq=[]
    while seq_1 and seq_2:
        if seq_1[0]<seq_2[0]:
            seq.append(seq_1.pop(0))
        else:
            seq.append(seq_2.pop(0))
    return seq+seq_1+seq_2
    

def merge_sort(seq,start,end):
    mid=(start+end)/2
    if start==end:
        return [seq[start]]
    seq_first=merge_sort(seq,start,mid)
    seq_second=merge_sort(seq,mid+1,end)
    seq=merge(seq_first,seq_second)
    return seq


alist=[0,-1,3,5,1,6,2,7,9]
print 'list before sorting is', alist
print 'list after merge-sort is', merge_sort(alist,0,len(alist)-1)