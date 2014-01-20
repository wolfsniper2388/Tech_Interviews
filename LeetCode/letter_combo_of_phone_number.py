''' Given a digit string, return all possible letter combinations that the number could represent.
    A mapping of digit to letters (just like on the telephone buttons) is given below.
    2: abc
    3: def
    4: ghi
    5: jkl
    6: mno
    7: pqrs
    8: tuv
    9: wxyz
    
    E.g
        Input: '23'
        Output: ['ad','ae','af','bd','be','bf','cd','ce','cf']
'''

letter_tuples=[(0,' '), (2,'abc'), (3,'def'), (4,'ghi'), (5,'jkl'),(6,'mno'), (7,'pqrs'),(8,'tuv'), (9,'wxyz')]
letter_hash = dict(letter_tuples)

def letter_combo(num_str, combos, curr_combo, curr_index):
    ''' find all possible letter combinations given the num_str
    '''
    if curr_index == len(num_str):
        combos.append(''.join(curr_combo))
        return combos
    for ch in letter_hash[int(num_str[curr_index])]:
        curr_combo.append(ch)
        letter_combo(num_str, combos, curr_combo, curr_index+1)
        # 'agh' -> 'ag'
        curr_combo.pop()
    return combos

if __name__=='__main__':
    test_cases=['792','24','305']
    for each_test_case in test_cases:
        print each_test_case, letter_combo(each_test_case, [],[],0)
    