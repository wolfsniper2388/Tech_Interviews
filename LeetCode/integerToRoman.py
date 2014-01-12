''' Given an integer, convert it to a Roman numeral.
    Input is guaranteed to be within the range from 1 to 3999
    I: 1
    V: 5
    X: 10
    L: 50
    C: 100
    D: 500
    M: 1000
    
    e.g
        4: IV
        9: IX
        40: XL
        2614: MMDCXIV 
'''

ROMAN_LETTER=['I','V','X','L','C','D','M','','']
ROMAN_PATTER=['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']

def pattern_matching(digit, one, five, ten):
    ''' 
        @return: a list of chars of the roman representation of digit
        digit cannot be 0
        e.g. (4, 'C', 'D', 'M') will return ['C','D']
             (7, 'X', 'L', 'C') will return ['L','X','X']
    '''
    roman_ch_list=[]
    pattern=ROMAN_PATTER[digit-1]
    for each_letter in pattern:
        if each_letter == 'I':
            roman_ch_list.append(one)
        elif each_letter == 'V':
            roman_ch_list.append(five)
        else:
            roman_ch_list.append(ten)
    return roman_ch_list


def int_to_roman_1(num):
    result_letters=[]
    div=1000
    letter_index=6  # point to M at first
    while div>0:
        curr_digit=num/div
        if curr_digit>0:
            curr_letters=pattern_matching(curr_digit, ROMAN_LETTER[letter_index], 
                             ROMAN_LETTER[letter_index+1], ROMAN_LETTER[letter_index+2])
            result_letters+=curr_letters
        num = num % div
        div= div/10
        letter_index-=2
    return ''.join(result_letters)


def int_to_roman_2(num):
    roman='IVXLCDM'
    div=1000
    result=[]
    # i is the index of roman, i = 6, 4, 2, 0.
    for i in range(6, -1, -2):
        curr_digit = num/div
        if curr_digit == 0:
            div/=10
            continue
        elif curr_digit <= 3:
            # add curr_digit number of roman[i]
            result.extend([roman[i]*curr_digit])
        elif curr_digit == 4:
            result.extend([roman[i], roman[i+1]])
        elif curr_digit == 5:
            result.append(roman[i+1])
        elif curr_digit <= 8:
            result.append(roman[i+1])
            result.extend([roman[i]*(curr_digit-5)])
        else:
            result.extend([roman[i], roman[i+2]])
        num%=div
        div/=10
    
    return ''.join(result)



if __name__=='__main__':
    for i in [1, 6, 9, 15, 40, 2014, 2634]:
        print 'method 1', i, int_to_roman_1(i)
        print 'method 2', i, int_to_roman_2(i)
        
            
    