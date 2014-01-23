''' The count-and-say sequence is the sequence of integers beginning as follows:
    1, 11, 21, 1211, 111221, ...

    1 is read off as "one 1" or 11.
    11 is read off as "two 1s" or 21.
    21 is read off as "one 2, then one 1" or 1211.
    Given an integer n, generate the nth sequence.

    Note: The sequence of integers will be represented as a string.
''' 

def count_and_say(n):
    last_str = '1'
    while n>0:
        curr_ch_list=[]
        prev_ch = last_str[0]
        count = 1
        for curr_ch in last_str[1:]:
            if curr_ch == prev_ch:
                count+=1
            else:
                curr_ch_list.append(str(count))
                curr_ch_list.append(prev_ch)
                count = 1
                prev_ch = curr_ch
        curr_ch_list.append(str(count))
        curr_ch_list.append(prev_ch)
        last_str = ''.join(curr_ch_list)
        n-=1
    return last_str

if __name__=='__main__':
    for n in range(18):
        print n, count_and_say(n)