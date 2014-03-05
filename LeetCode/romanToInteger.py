''' Given a Roman numeral, convert it to an integer.
    Input is guaranteed to be within the range from 1 to 3999.
    Note: one way to validate the Roman numerals is to use the following regular expression:
        ^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$
'''


def roman_to_int(s):
    roman_tuples=(('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100), ('D', 500), ('M', 1000))
    map=dict((x,y) for x,y in roman_tuples)
    prev=None
    ch=s[0]
    num=map[ch]
    i=1
    while i<len(s):
        prev=ch
        ch=s[i]
        num+=map[ch]
        if map[prev]<map[ch]:
            num-=2*map[prev]
        i+=1
    return num
        
if __name__=='__main__':
    for roman in ['I', 'VI', 'IX', 'XV', 'XL', 'MMXIV', 'MMDCXXXIV']:
        print roman, roman_to_int(roman)
    