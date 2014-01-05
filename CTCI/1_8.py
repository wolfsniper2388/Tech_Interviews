''' check if a string a rotation of another string
    Example:
    Input: 'waterbottle', 'erbottlewat'
    Output: True
    Input: 'waterbottle', 'bottleretaw'
    Output: False
'''

# check if str2 is a rotation of str1
def is_rotation(str1,str2):
    if not str1 or not str2 or len(str2)!=len(str1):
        return False
    return str2 in str1+str1

if __name__=='__main__':
    print is_rotation('waterbottle','erbottlewat')
