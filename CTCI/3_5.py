''' Implement a queue class using two stacks
'''


''' When doing popleft/get_front back to back. This approach has no 
    need to move elements back and forth.
    When the popleft command comes, simply pop the st2's top
    When the get_front command comes, simply return the st2's top
    If st2 is empty, infuse st2 with elements in st1
    If both are empty, the queue is empty
    
'''
class MyQueue(object):
    def __init__(self):
        self.st1=[]      # st1 holds the newest elements on top
        self.st2=[]      # st2 holds the oldest elements on top
    
    def shift(self):
        if not self.st2:
            while self.st1:
                self.st2.append(self.st1.pop())
                
    def append(self,data):
        self.st1.append(data)
        
    def popleft(self):
        self.shift()
        if not self.st2:
            print 'Queue is empty. Cannot popleft'
            return
        self.st2.pop()
        
    def get_front(self):
        self.shift()
        if not self.st2:
            print 'Queue is empty. No front element'
            return
        return self.st2[-1]
        
        
if __name__=='__main__':
    q=MyQueue()
    for i in range(10):
        q.append(i)
    print q.get_front()
    for i in range (12):
        q.popleft()
        print q.get_front()
        