''' Given a Roman numeral, convert it to an integer.
    Input is guaranteed to be within the range from 1 to 3999.
    Note: one way to validate the Roman numerals is to use the following regular expression:
        ^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$
'''


def roman_to_int(s):
    roman_tuples=(('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100), ('D', 500), ('M', 1000))
    map=dict((x,y) for x,y in roman_tuples)
    num = map[s[0]]
    prev_ch = s[0]
    for curr_ch  in s[1:]:
        num += map[curr_ch]
        if map[curr_ch] > map[prev_ch]:
            num -= 2*map[prev_ch]
        prev_ch = curr_ch
    return num
        
if __name__=='__main__':
    for roman in ['I', 'VI', 'IX', 'XV', 'XL', 'MMXIV', 'MMDCXXXIV']:
        print roman, roman_to_int(roman)
    