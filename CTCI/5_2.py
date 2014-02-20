''' represent a double number from 0 to 1 (e.g. 0.72) as a binary, if it cannot be represented with at most 32 chars, return 'ERROR'
'''

def bin_repr(x):
    binary = ['0','.']
    div = 0.5
    counter=0
    while x>0:
        if counter == 32:
            return 'ERROR'
        if x >= div:
            binary.append('1')
            x-=div
        else:
            binary.append('0')
        div/=2
        counter+=1
    return ''.join(binary)

if __name__=='__main__':
    test_cases = [0.5,0.25,0.125,0.75,0.375,0.625,0.98]
    for each_test_case in test_cases:
        print bin_repr(each_test_case)
        
    