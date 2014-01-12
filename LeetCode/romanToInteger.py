''' Given a roman numeral, convert it to an integer.
    Input is guaranteed to be within the range from 1 to 3999.
'''
roman_tuples=(('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100), ('D', 500), ('M', 1000))
roman_hash=dict((x,y) for x,y in roman_tuples)

def roman_to_int(roman):
    ans=0
    last_int=9999
    for curr_ch in roman:
        curr_int=roman_hash[curr_ch]
        # add to ans anyway
        ans+=curr_int
        # deal with 4 and 9
        if curr_int > last:
            ans -= 2*last
        last = curr_int
    return ans 
    
    
    
if __name__=='__main__':
    for roman in ['I', 'VI', 'IX', 'XV', 'XL', 'MMXIV', 'MMDCXXXIV']:
        print roman, roman_to_int(roman)
    