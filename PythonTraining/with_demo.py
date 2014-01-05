''' Gain sophisticated understanding of the with-statement
    and ContextManagers (which means 'with-able')
    which have __enter__ and __exit__ methods
'''

import threading

#The OLD way of printing length of file
f=open("c:\\notes\\hamlet.txt")
try:
    play=f.read()
    print len(play)
finally:
    f.close()

#The NEW way of printing length of file
with open("c:\\notes\\hamlet.txt") as f:    # make a setup context: open a file and close a file, what happened inside is in the context
    play=f.read()
    print len(play)
    
# How to make a lock
print_lock=threading.Lock()

#How to use a lock the OLD way
print_lock.acquire()
try:
    print 'Critical section 1'
    print 'Critical section 2'
finally:
    print_lock.release()        #must always rerealse the lock


#How to use a lock the NEW way
with print_lock:
    print 'Critical section 1'
    print 'Critical section 2'

# How to make a generic context manager
class CM:
    'A generic context manager class'
    def __init__(self,x):
        print 'Initializing with', x
        self.x=x
    
    def __enter__(self):
        print 'Entering the CM'
        print 'We still know x:', self.x
        return 42
    
    def __exit__(self,exctype,excinst,exctb):       #exception type, exception instance, exception traceback
        print 'Exiting the CM'
        print 'Exctype is', exctype
        if exctype == KeyError:
            print 'Caught a KeyError'
            print 'Args: ', excinst.args
            print 'Marking as handled'
            return True
        print 'Not marking as handled'
        return None
        
# The first path is the normal path with no error
print 'Starting up'
with CM(10) as y:       # hit __enter__, the return value 42 is passed to y 
    print 'In the body with', y
    print 'In the middle'
    print 'Leaving the body'
                        # hit __exit__
print 'Wrapping up'
        
        
        
# The second path is the handled exception path
print 'Starting up'
with CM(10) as y:       
    print 'In the body with', y
    print 'In the middle'
    raise KeyError('roger')
    print 'Leaving the body Never get here'
print 'Wrapping up'

'''
# The third path is the handled exception path
print 'Starting up'
with CM(10) as y:       
    print 'In the body with', y
    print 'In the middle'
    raise IndexError(10)
    print 'Leaving the body Never get here'         
print 'Wrapping up'
'''

'''
with open("c:\\notes\\hamlet.txt") as f:    
    play=f.read()
    print len(play)
'''

# Inside file objects

class File:
    def __init__(self,filename,mode='r',flags=0644):
        pass
    def read(self, n=None):
        pass
    def write(self):
        pass
    def close(self):
        pass
    def __enter__(self):
        return self
    def __exit__(self,exctype,excinst,exctb):
        self.close()
'''
with print_lock:
    print 'Critical section 1'
    print 'Critical section 2'       
'''
                
# Inside lock objects

class Lock:
    def __init__(self):
        pass
    def __acquire(self):
        pass
    def __release(self):
        pass
    def __enter__(self):
        self.acquire()
        return self
    def __exit__(self,exctype,excinst,exctb):
        self.release()
        




# How to wrap existing objects to make them Context Manager

class Closing:
    ''''Add auto-closing capability to an existing object
        that already has a close() method
     '''
    
    def __init__(self,obj):
        self.obj=obj
        
    def __enter__(self):
        return self.obj
    
    def __exit__(self,exctype,excinst,exctb):
        self.obj.close()
        
from StringIO import StringIO

# The old way of using StringIO
f=StringIO()
f.write('hello\n')
f.write('goodbye\n')
print f.getvalue()

# The new way of using StringIO
with Closing(StringIO()) as f:
    f.write('hello\n')
    f.write('goodbye\n')
    print f.getvalue()
    


# How to redirect prints

import sys


class RedirectStdOut:
    
    def __init__ (self,tgtfile):
        self.tgtfile=tgtfile
    
    def __enter__(self):
        self.oldstdout=sys.stdout
        sys.stdout=self.tgtfile     # When entering the context manager, change the system stdout to tgtfile
        
    def __exit__(self,exctype,excinst,exctb):
        sys.stdout=self.oldstdout       # When leaving the context manager, change the system stdout back to stdout



# ==================================Test ======================================
def foo(x):
    if x==3:
        x=5
    return x*x

from dis import dis

with RedirectStdOut(sys.stderr):
    dis(foo)
    
# Nested with statement

with open('dis.txt', 'w') as f:
    with RedirectStdOut(f):
        dis(foo)

# StringIO: something working with file, we want it working with String instead
with Closing(StringIO()) as f:
    with RedirectStdOut(f):
        help(pow)
    s=f.getvalue()

print s

