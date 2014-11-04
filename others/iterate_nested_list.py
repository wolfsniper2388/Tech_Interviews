''' iterate through a nested list
    e.g. 
        input: A = [1,2,[3,[4,5],6],7,[],[8]]
'''

def traverse(A):
    for elem in A:
        if isinstance(elem, int):
            print elem,
        else:
            traverse(elem)
            

if __name__=='__main__':
    test_cases =[[1,2,[3,[4,5],6],7,[],[8]], [1,2,3]]
    for each_test_case in test_cases:
        print each_test_case
        traverse(each_test_case)
        print