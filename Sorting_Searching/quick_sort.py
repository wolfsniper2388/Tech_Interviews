''' Implement quick sort
'''

from random import randint

def quick_sort(pass_in_seq):
    quick_sort_helper(pass_in_seq,0,len(pass_in_seq)-1)


''' p | <p | >p | unpartitioned
      i    j
    step1     3 8 2 5 1 4 7 6
                i
                j
    step2    3 8 2 5 1 4 7 6
               i j
             3 2 8 5 1 4 7 6
                 i
                 j
    step3    3 8 2 5 1 4 7 6
                 i j          
    step3    3 2 8 5 1 4 7 6
                 i   j
             3 2 1 5 8 4 7 6
                   i j
    step4    3 2 1 5 8 4 7 6
                   i   j
    step5    3 2 1 5 8 4 7 6
                   i     j
    step6    3 2 1 5 8 4 7 6
                   i       j
                   
    step7    1 2 3 5 8 4 7 6    # swap seq[start], seq[i-1]
                   i       j         
            
'''
def quick_sort_helper(seq, start, end):
    if start >= end:
        return
    # randomly select the pivot index, and swap it with the 1st element
    pivot_index=randint(start,end)
    seq[start],seq[pivot_index]=seq[pivot_index],seq[start]
    pivot=seq[start]
    i=start+1
    for j in range(start+1,end+1):
        if seq[j] < pivot:
            seq[i],seq[j]=seq[j],seq[i]
            i+=1
    seq[i-1],seq[start]=seq[start],seq[i-1]
    quick_sort_helper(seq, start,i-2)
    quick_sort_helper(seq,i,end)
        
    
if __name__=='__main__':
    seq=[3,8,2,5,1,4,3,6]
    quick_sort(seq)
    print seq