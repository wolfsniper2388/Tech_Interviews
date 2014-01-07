''' Implement a stack with O(1) time operation of push, pop and get_min
'''


class Magic_Stack (object):
    def __init__(self):
        self.element=[]
        self.min=[]
    
    ''' always push to element
        only when min is not empty and x < min[-1], push to min
    '''
    def push(self, x):
        self.element.append(x)
        if not self.min or x<self.min[-1]:
            self.min.append(x)
    
    ''' always pop element
        only when element[-1] == min[-1], pop min
    '''
    def pop(self):
        if not self.element:
            print 'The stack is empty. Cannot pop'
            return 
        if self.element[-1]==self.min[-1]:
            self.min.pop()
        self.element.pop()
        
    def get_min(self):
        if not self.min:
            print 'The stack is empty. No min number'
            return
        return self.min[-1]
    
if __name__=='__main__':
    s=Magic_Stack()
    for i in [5,3,2,7,1,8]:
        s.push(i)
    for i in range(6):
        print s.get_min()
        s.pop()
    s.pop()
    print s.get_min()
