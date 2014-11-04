''' Given an absolute path for a file (Unix-style), simplify it.
    E.g.
        Input: '/home/'
        Output: '/home'
        Input: '/a/./b/../../c/'
        Output: '/c'
        Input: '/../'
        Output: '/'
        Input: '/home//foo'
        Output: '/home/foo'
'''

def simplify_path(path):
    stack = []
    i = 0
    while i < len(path):
        while i < len(path) and path[i] == '/':
            i+=1
        # if i hits the end, jump out of the whole while loop
        if i == len(path):
            break
        # after while loop, i is the start of char
        start = i
        while i < len(path) and path[i]!='/':
            i+=1
        end = i-1
        each_dir = path[start:end+1]
        if each_dir == '..':
            if stack:
                stack.pop()
        elif each_dir != '.':
            stack.append(each_dir)
    if not stack:
        return '/'
    result_path = []
    while stack:
        result_path.append('/'+stack.pop())
    result_path.reverse()
    return ''.join(result_path)

if __name__=='__main__':
    test_cases = ['/home/', '/home//foo', '/work/./jas_feng//../../ws', '/../..', '/a/./b/../../c/', '/..', 'a/b/cd']
    for each_test_case in test_cases:
        print each_test_case, simplify_path(each_test_case)
        
        
        